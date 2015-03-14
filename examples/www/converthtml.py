#!/usr/bin/python


import sys, re, urlparse, urllib

class NullParser:
    "just copies data"
    def __init__(self):
        self.output_buffer = ''

    def feed(self, data):
        self.output_buffer += data

    def close(self):
        pass
        
    def pull(self):
        r = self.output_buffer
        self.output_buffer = ''
        return r


class BasicParser:

    def __init__(self):
        self.in_tag = False
        self.current_tag = ''
        self.current_data = ''
        
    def feed(self, data):
        self.process(data)

    def process(self, txt):
        for c in txt:
            if self.in_tag:
                self.current_tag += c
                if c=='>':
                    self.process_tag(self.current_tag)
                    self.in_tag = False
                    self.current_tag = ''
            else:
                assert not self.current_tag
                if c != '<':
                    self.current_data += c
                else:
                    self.process_data(self.current_data)
                    self.in_tag = True
                    self.current_data = ''
                    self.current_tag = c # i.e., <

    def close(self):
        if self.in_tag: # open < at the and of dosument
            assert self.current_tag
            self.process_tag(self.current_tag)
        else:
            self.process_data(self.current_data)

    def process_tag(self, tagstr):
        "to be subclassed"
        return tagstr
        
    def process_data(self, datastr):
        "to be subclassed"
        return datastr


class CopyParser(BasicParser):

    def __init__(self):
        self.output_buffer = ''
        BasicParser.__init__(self)

    def process_tag(self, tagstr):
        "to be subclassed"
        self.output_buffer += tagstr
        
    def process_data(self, datastr):
        "to be subclassed"
        self.output_buffer += datastr
        
    def pull(self):
        r = self.output_buffer
        self.output_buffer = ''
        return r

class CopyAndModifyParser(CopyParser):            
    def __init__(self):
        self.in_script = False
        self.in_style = False
        CopyParser.__init__(self)

    def process_tag(self, tagstr):
        newtag = self.modify_tag(tagstr)
        self.output_buffer += newtag
        if re.match(r'(?is)<script\b(?!.*?/\s*>)', tagstr):
            self.in_script = True
        elif re.match(r'(?is)</script\b', tagstr):
            self.in_script = False
        if re.match(r'(?is)<style\b(?!.*?/\s*>)', tagstr):
            self.in_style = True
        elif re.match(r'(?is)</style\b', tagstr):
            self.in_style = False
        
    def process_data(self, datastr):
        if self.in_script or self.in_style: # do not modify data inside <script></script> tags...
            newdata = datastr
        else:
            newdata = self.modify_data(datastr)
        self.output_buffer += newdata
    
    def modify_tag(self, tagstr):
        "to be subclassed"
        return tagstr

    def modify_data(self, datastr):
        "to be subclassed"
        return datastr

# inspired from feedparser by Mark Pilgrim
relative_uris = {
                     'a': ('href',),
                     'applet': ('codebase',),
                     'area': ('href',),
                     'blockquote': ('cite',),
                     'body': ('background',),
                     'del': ('cite',),
                     'form': ('action',),
                     'frame': ('longdesc', 'src'),
                     'iframe': ('longdesc', 'src'),
                     'head': ('profile',),
                     'img': ('longdesc', 'src', 'usemap'),
                     'input': ('src', 'usemap'),
                     'ins': ('cite',),
                     'link': ('href',),
                     'object': ('classid', 'codebase', 'data', 'usemap'),
                     'q': ('cite',),
                     'script': ('src',)
                }

_urifixer = re.compile('^([A-Za-z][A-Za-z0-9+-.]*://)(/*)(.*?)')
def _urljoin(base, uri):
    uri = _urifixer.sub(r'\1\3', uri)
    return urlparse.urljoin(base, uri)

def get_uri_tag_value(tagstr, k):
    "try to get value of 'k' attribute from a given html tag"
    m = re.search(r"""\b%s\=['"](.*?)['"]""" % k, tagstr, re.I+re.S)
    if not m: # not in quotes? hmm...
        m = re.search(r"""\b%s\=(.*?)\s(?=\>)""" % k, tagstr, re.I+re.S)
    if not m: # nothing found
        return None
    return m.start(), m.end(), m.group(1)


class ModifyHrefParser(CopyAndModifyParser):
    # also rewrite href's to go through our cgi script
    def __init__(self, cgi_url, base_url):
        self.cgi_url = cgi_url
	self.base_url = base_url
        CopyAndModifyParser.__init__(self)

    def modify_tag(self, tagstr):
        "NOT to be subclassed"
        if not self.cgi_url:
            return tagstr
        m = re.search(r'<([A-Za-z]+?)\b', tagstr, re.S)
        if m:
            tag = m.group(1)
	    if tag.lower()=='a':
                spanval = get_uri_tag_value(tagstr, 'href')
                if spanval: # found, we need to replace the reference
                    start, end, val = spanval
		    url = _urljoin(self.base_url, val)
                    newval = self.cgi_url+'?'+'url='+urllib.quote_plus(url, safe='')
                    tagstr = tagstr[:start]+''+'href'+'="'+newval+'"'+tagstr[end:]
        return tagstr



class MyParser(ModifyHrefParser):

    def modify_data(self, datastr):
        return re.sub('[a-z]', 'a', datastr)

if __name__=='__main__':
    filehandle = open('a.html', 'r')
    parser = MyParser(base_url='http://www.sme.sk')
    while True:
        data = filehandle.read(1000)               # read in the data in chunks
        if not data: break                      # we've reached the end of the file - python could do with a do:...while syntax...
        parser.feed(data)
        sys.stdout.write(parser.pull())                     # you can output data whilst processing using the push method
    #processedfile = parser.close()              # or all in one go using close  
    parser.close()                       # Even if using push you will still need a final close
    sys.stdout.write( parser.pull())
    filehandle.close()
