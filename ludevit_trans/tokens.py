#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# simple text tokenization
# words are split at all the non-alphanumeric characters
# if used as a stand-alone utility, input and output is meant to be in utf-8

import unicodedata

lowercase = 'aáäbcčdďeéfghiíjklľĺmnňoóôprŕsštťuúvwxyýzž'
uppercase = 'AÁÄBCČDĎEÉFGHIÍJKLĽĹMNŇOÓÔPRŔSŠTŤUÚVWXYÝZŽ'
slovak_letters = lowercase+uppercase

def IsSlovak(s):
    "test if string is a slovak word"
    for c in s:
        if c not in slovak_letters:
            return False
    return True

def IsLetter(c):
#    if c in "-@\u2010":
#    	return True
#    print `c`
    category = unicodedata.category(c)
    return category[0] in 'LMN'

def IsWs(c):
    # eventualy, if your input texts have rich unicode formatting,
    # add other types of spaces here (such as ETHIOPIC WORDSPACE, EN SPACE ....)
    return c in " \t\n\r\u00a0"

def make_tokens(text):
    ws = '' # whitespace in front of each token
    word = ''
    for c in text:
        if IsLetter(c):
            word += c
        elif IsWs(c):
            if word:
                yield word, ws
                word = ''
                ws = ''
            ws += c
        else:
            if word:
                yield word, ws
                word = ''
                ws = ''
            yield c, ws
            ws = ''
    if word or ws:
        yield word, ws

if __name__ == '__main__':
    import fileinput
    for line in fileinput.input():
        for token, ws in make_tokens(line):
            print (token, repr(ws))

