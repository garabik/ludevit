#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unicodedata

from translate import Translate
from tokens import make_tokens, IsSlovak

class Word:
    def __init__(self, token, ws):
        self.token = token
        self.ws = ws

    def __str__(self):
        return self.ws+self.token


def parse_text(text):
    for tok, ws in make_tokens(text):
        yield Word(tok, ws)

def words2text(words):
    r = ''
    for w in words:
        r += unicode(w)
    return r


class Translator:

    def __init__(self, table_voc, table_ort, postprocess=None):
	self.translate = Translate(table_voc, table_ort, postprocess)

    def translate_words(self, words):
        for w in words:
            orig = w.token
            if IsSlovak(orig):
                nw = Word(self.translate.trans(orig), w.ws)
            else:
                nw = w
            yield nw

    def translate_text(self, text, nfkd='none'):
        words =  parse_text(text)
        words = self.translate_words(words)
        text = words2text(words)
        if nfkd=='all':
            text = unicodedata.normalize('NFKD', text)
        elif nfkd=='hack':
            text = text.replace(u'ď', u'd\N{COMBINING CARON}').replace(u'ť', u't\N{COMBINING CARON}')
        return text


if __name__ == '__main__':
    import tables_ludevit
    translator = Translator(tables_ludevit.table_voc, tables_ludevit.table_ort, tables_ludevit.postprocess)

    import fileinput
    for line in fileinput.input():
        t =  translator.translate_text(line.decode('utf-8'))
        print t
        
            
