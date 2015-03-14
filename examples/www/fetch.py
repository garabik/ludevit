#!/usr/bin/python

import urllib2
import re
import socket
from htmlentitydefs import name2codepoint

# one minute default timeout for everything - ugly, but urllib2 does not expose timeout API for sockets...
socket.setdefaulttimeout(60)

from ludevit_trans.translator import Translator
from ludevit_trans import tables_ludevit

from converthtml import ModifyHrefParser, NullParser


# read page in chunks of this size
CHUNKSIZE = 5000

# size of the first chunk, used to guess charset and add base url
FIRSTCHUNKSIZE = 5000

BASE_CGI='http://www.juls.savba.sk/ludevit/'

def _replace_entity(m):
     s = m.group(1)
     if s[0] == u'#':
         s = s[1:]
         try:
             if s[0] in u'xX':
                 c = int(s[1:], 16)
             else:
                 c = int(s)
             return unichr(c)
         except ValueError:
             return m.group(0)
     else:
         try:
             return unichr(name2codepoint[s])
         except (ValueError, KeyError):
             return m.group(0)

_entity_re = re.compile(r"&(#?[xX]?(?:[0-9a-fA-F]+|\w{1,8}));")
def unescape_entities(s):
     return _entity_re.sub(_replace_entity, s)


class LudevitParser(ModifyHrefParser):

    def __init__(self, encoding, cgi_url, base_url):
        self.encoding = encoding
        ModifyHrefParser.__init__(self, cgi_url, base_url)
        self.translator = Translator(tables_ludevit.table_voc, tables_ludevit.table_ort, tables_ludevit.postprocess)

    
    def modify_data(self, datastr):
    
        # re-encoding here is slow, as compared with encoding the whole chunk
        # before feeding it to the parser
        # however, this deals better with the rare case of non-ascii characters
        # in href's URLs...
        txt = datastr.decode(self.encoding, 'replace')
        txt = unescape_entities(txt)
        tran = self.translator.translate_text(txt)
        tran = tran.encode(self.encoding, 'xmlcharrefreplace')
        return tran


def guess_charset_from_meta(txt):
    charset = None
    m = re.search(r'meta\s*http-equiv\="Content-Type"\s*content\="text/html;\s*charset\=(.+?)"', txt, re.I+re.S)
    if m:
        charset = m.group(1)
    return charset

def guess_if_base(txt):
    "find out if there is a BASE URL in the html page"
    return re.search(r'base\s*href\=', txt, re.I+re.S)


def report_error(text):
    headers = 'Content-Type: text/plain\r\n'
    body = 'An error has occurred: ' + text +'\nOops.\n'
    return headers, body    

def prepare_page(url, user_agent):
    "open url, read some bytes (to guess charset)"

    do_add_base_url = False
    
    # sanity checks
    if len(url)>512:
        charset = 'us-ascii'
        headers, first_chunk = report_error('Overlong URL')
        f = None
        return False, charset, headers, first_chunk, f, do_add_base_url
    protocol = url[:10]
    if ':' not in protocol:
        charset = 'us-ascii'
        headers, first_chunk = report_error('Invalid protocol')
        f = None
        return False, charset, headers, first_chunk, f, do_add_base_url
    protocol = protocol.split(':')[0]
    protocol = protocol.lower()
    if protocol not in ['http', 'https', 'ftp', 'gopher']:
        charset = 'us-ascii'
        headers, first_chunk = report_error('Unsupported protocol')
        f = None
        return False, charset, headers, first_chunk, f, do_add_base_url
    req = urllib2.Request(url)
    req.add_header('User-Agent', user_agent)
    try:
        f = urllib2.urlopen(req)
    except urllib2.HTTPError:
	# redir to original url
        headers = 'Location: %s\r\n' % url
        charset = 'us-ascii'
        first_chunk = ''
        f = None
        return False, charset, headers, first_chunk, f, do_add_base_url
    except urllib2.URLError, exc:
        charset = 'us-ascii'
        headers, first_chunk = report_error(str(exc))
        f = None
        return False, charset, headers, first_chunk, f, do_add_base_url

    resp_info = f.info()
    del resp_info['Content-Length']
    headers = ''.join(resp_info.headers)
    ct = f.info().get('Content-Type', '')
    do_translate = ct.lower().startswith('text')
    if not do_translate:
        return False, None, headers, '', f, do_add_base_url

    charset_from_headers = None
    if ct:
        fields = ct.split(';')
        for field in fields:
            fs = field.strip()
            if fs.lower().startswith('charset='):
                charset_from_headers = fs[len('charset='):].strip().lower()
                break
    first_chunk = f.read(FIRSTCHUNKSIZE)

    charset_from_meta = guess_charset_from_meta(first_chunk)
    charset = charset_from_headers or charset_from_meta
#    if charset_from_meta and charset_from_headers and (charset_from_meta != charset_from_headers):
        # we should honour the charset form headers, as per http standard
	# this code was clever, but e.g. www.nku.gov.sk fails the test
        #if 'windows-1250' in [charset_from_meta, charset_from_headers]:
        #    charset = 'windows-1250'
        #elif 'iso-8859-2' in [charset_from_meta, charset_from_headers]:
        #    charset = 'iso-8859-2'
        # there could be cp852 or MacRoman2 test here, but who uses such encodings nowadays?
        # some do, but let's assume they do not differ in headers and meta...
#        else:
#            charset = charset_from_meta # not standard conforming, but probably better

    # fallback, if everything failed
    if not charset:
        charset = 'windows-1250'

    if ct.lower().startswith('text/html') and not guess_if_base(first_chunk): # if a base url is present in the original html, do not add another one...
        do_add_base_url = True
    
    return True, charset, headers, first_chunk, f, do_add_base_url


def add_base_url(chunk, base):
    "try to find <head> element and add a <base href=...> tag into it"
    bastag = '<base href="%s" />'%base
    headtag = '<head>'+bastag+'</head>'
    if re.search(r'<head\b.*?>', chunk, re.I+re.S):
	r = re.sub(r'(?i)(<head\b.*?>)', r'\1'+bastag, chunk)
    # try to add head
    elif re.search(r'<html\b.*?>', chunk, re.I+re.S):
	r = re.sub(r'(?i)(<html\b.*?>)', r'\1'+headtag , chunk)
    elif chunk.startswith('<!'):
	r = re.sub(r'(<\!.*?>)', r'\1'+headtag, chunk)
    else:
	# no <head>, no <!doctype>, ho <html>... just add it
	r = headtag+chunk

    return r
	

def translate_page(url, user_agent):
    pp = prepare_page(url, user_agent)
    do_translate, charset, headers, chunk, f, do_add_base_url = pp
    yield headers
    yield '\r\n'

    if do_translate:
        if do_add_base_url:
            # use the page as base url
            base = f.geturl() # in case of redirect
            chunk = add_base_url(chunk, base)
        else:
            base = ''
        parser = LudevitParser(charset, BASE_CGI, base)
    else:
        parser = NullParser()

    while f: # f could be None to signalize the url has not been successfuly opened
        newchunk = f.read(CHUNKSIZE)
        if not newchunk:
            break
        chunk += newchunk
        # we have to be careful not to tear utf-8 characters apart...
        if ord(chunk[-1])<128:
            parser.feed(chunk)
            chunk = ''
            yield parser.pull()
    parser.feed(chunk)
    parser.close()
    yield parser.pull()


if __name__=='__main__':

    import sys
    url = sys.argv[1]
    user_agent = sys.argv[2]
    for c in translate_page(url, user_agent):
        sys.stdout.write(c)
