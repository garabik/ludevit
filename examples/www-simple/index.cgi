#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import cgi, sys, codecs, time, random, os

from ludevit_trans.translator import Translator
from ludevit_trans import tables_ludevit


logdir='/var/log/ludevit/'


def writelog(text):
    "write text to a logfile, text is a plain 8-bit string, not unicode"
    if not logdir or not text:
        return
    remote_addr = os.environ.get('REMOTE_ADDR', '')
    try:
        if not os.path.exists(logdir):
            os.makedirs(logdir)
        fname = time.strftime('%Y%m%d_%H%M%S', time.gmtime())+'_%0x'%random.randint(0,0xff)
        fname = os.path.join(logdir, fname)
        f = file(fname, 'w')
        f.write(remote_addr+'\n')
        f.write(text)
        f.close()
    except (IOError, OSError):
        pass
    return

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
Vaše názori posjelajťe na adresu <strong>ludevit @ juls.savba.sk</strong>
</p>
</body>
</html>
'''

def form(text='', nfkd='none'):
    text = cgi.escape(text)
    r = u'''
<form action="" method="post">
<textarea name="text" cols="70" rows="20" wrap="soft">%s</textarea>
''' % text
    if nfkd<>'none':
        checked = 'checked'
    else:
        checked = ''
    r += u'''
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

def format_translation(text):
    if not text:
        return ''
    r = '''<div>
%s
</div><hr />''' % cgi.escape(text).replace('\n', '<br />')
    return r

sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

print "Content-type: text/html"     # HTML is following
print                               # blank line, end of headers


print header()

f = cgi.FieldStorage()

text = f.getfirst("text", "kokot")
do_nfkd = f.getfirst("nfkd", False)
nfkd = 'none'
if do_nfkd:
    nfkd = 'hack'

if text:
    writelog(text)
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
else:
    t = u'''
Toto je automatickí prekladač textu zo spisovnej Slovenčini do štúrovskej.
Napíšťe krátki text v spisovnom nárečí so správnou diakritikou a klikňiťe na «prelož».
'''
    print format_translation(t)

print form(text='', nfkd=nfkd)

print footer()

