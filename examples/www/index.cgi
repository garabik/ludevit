#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import cgi, sys, codecs, time, random, os

from ludevit_trans.translator import Translator
from ludevit_trans import tables_ludevit


from fetch import translate_page

logdir='/var/log/ludevit/'

def writelog(text):
    "write text to a logfile, text is a plain 8-bit string, not unicode"
    if not logdir or not text:
        return
    remote_addr = os.environ.get('REMOTE_ADDR', '')
    logdir_now = os.path.join(logdir, time.strftime('%Y-%m-%d', time.gmtime()))
    try:
        if not os.path.exists(logdir_now):
            os.makedirs(logdir_now)
        fname = time.strftime('%Y%m%d_%H%M%S', time.gmtime())+'_%02x'%random.randint(0,0xff)
        fname = os.path.join(logdir_now, fname)
        f = file(fname, 'w')
        f.write(remote_addr+'\n')
        f.write(text)
        f.close()
    except (IOError, OSError):
        pass
    return

def get_user_agent():
    agent = os.environ.get('HTTP_USER_AGENT', 'Speccy/82 [en] (ZX Spectrum; U)')
    return agent


def header():
    r = u'''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="sk" xml:lang="sk">
<head>
    <title>ludevít</title>
    <meta http-equiv="Content-Type"
        content="text/html; charset=utf-8" />
    <link href="/pics/favicon-stur.ico" rel="shortcut icon" />

</head>

<body>
'''
    return r

def footer():
    return u'''
<p>
Pozri aj: <a href="/nrs/">Nauka reči Slovenskej</a>
</p>
<p>
Vaše názori posjelajťe na adresu <strong>ludevit @ juls.savba.sk</strong>
</p>
</body>
</html>
'''

def form(text='', nfkd='none'):
    text = cgi.escape(text)
    r = u'''
<form action="" method="post">
<textarea name="text" cols="70" rows="15" wrap="soft">%s</textarea>
''' % text
    if nfkd<>'none':
        checked = 'checked'
    else:
        checked = ''
    r += u'''
<br />
Alebo URL ktoruo chceťe preložiť:
<br/>
<input name="url" maxlength="500" size="70" value="http://" />
<br />
<input type="checkbox" name="nfkd" %s />Vísledok zobraz v NFKD normalizácii
<a href="/ludevit/why_nfkd.html">(prečo bi som mau?)</a>
''' % checked

    r += u'''
<br />
<input type="submit" value="prelož" />
</form>
''' 
    return r

def is_valid_url(url):
    "protection against malformed urls"
    # length restriciton
    if len(url)>2047:
	return False
    # and, an url should not contain control characters
    for c in url:
	if c<ord(' '):
	    return False
    return True

def fix_url(url):
    if url.startswith(r'http:\\'): # stupid, stupid
	url = url.replace('\\', '/')
    if '://' not in url:
	url = 'http://'+url
    return url

def format_translation(text):
    if not text:
        return ''
    r = '''<div>
%s
</div><hr />''' % cgi.escape(text).replace('\n', '<br />')
    return r

def init_headers():
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
    print "Content-type: text/html"     # HTML is following
    print                               # blank line, end of headers
    print header()

def formandfooter():
    print form(text='', nfkd=nfkd)
    print footer()

f = cgi.FieldStorage()

text = f.getfirst("text", "")
url = f.getfirst("url", "").strip()
do_nfkd = f.getfirst("nfkd", False)
nfkd = 'none'
if do_nfkd:
    nfkd = 'hack'

user_agent = get_user_agent()
robot = 'bot' in user_agent

if text and not robot:
    writelog(text)
    init_headers()
    try:
        text = unicode(text, 'utf-8')[:40000] # safeguard
        translator = Translator(tables_ludevit.table_voc, tables_ludevit.table_ort, tables_ludevit.postprocess)
        t = translator.translate_text(text, nfkd)
    except UnicodeDecodeError:
        t = u'''
Text ňebou v UTF-8 koduvaní. Možno váš browser ňepodporuje
UTF-8. Všetki modernje browseri toto podporujú, skúsťe novú versiu. Ibažebi
sťe k stránke ňepristupovali z običajnjeho počítača, ale z dajakjeho
inšjeho zarjaďeňja, napriklad z PDA, kďe browseri často UTF-8 aňi žjadne
Slovenskje písmeni ňepodporujú. To je nám lúto.
'''
    print format_translation(t)
    formandfooter()
elif url and url!='http://' and is_valid_url(url) and not robot:
    url = fix_url(url)
    writelog('URL "%s" || "%s"' % (url, user_agent))
    for c in translate_page(url, user_agent):
        sys.stdout.write(c)
    sys.exit(0)
else:
    init_headers()
    t = u'''
Toto je automatickí prekladač textu zo spisovnej Slovenčini do štúrovskej.
Napíšťe krátki text v spisovnom nárečí so správnou diakritikou a klikňiťe na «prelož».
'''
    print format_translation(t)
    formandfooter()

