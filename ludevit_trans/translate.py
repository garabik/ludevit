#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re, string
import tokens


class MultiReplace:

    def __init__(self, repl_dict):

	if not repl_dict:
	    self.replace = lambda x: x
	    return
        # string to string mapping; use a regular expression
        keys = repl_dict.keys()
        keys.sort() # lexical order
        keys.reverse() # use longest match first
        pattern = string.join(map(re.escape, keys), "|")
        self.pattern = re.compile(pattern)
        self.dict = repl_dict

    def replace(self, str):
        # apply replacement dictionary to string
        def repl(match, get=self.dict.get):
            item = match.group(0)
            return get(item, item)
        return self.pattern.sub(repl, str)




def tok2psre(tok):
    return '^'+tok+'$'

def psre2tok(s):
    assert len(s)>=2
    assert s[0]=='^' and s[-1]=='$'
    return s[1:-1]



class Translate:

    def __init__(self, table_voc, table_ort, postprocess=None):
	self.table_voc = table_voc
	self.table_ort = table_ort
	self.postprocess = postprocess
	self.mr_voc = MultiReplace(table_voc)
	self.mr_ort = MultiReplace(table_ort)

    def trans_voc(self, tok):
	return self.mr_voc.replace(tok)

    def trans_ort(self, tok):
	return self.mr_ort.replace(tok)


    def trans(self, tok):
        t = tok.lower()
        t = tok2psre(t)
        t = self.trans_voc(t)
        t = self.trans_ort(t)
        t = psre2tok(t)
        # now apply the uppercase mapping
        tl = list(t)
        for i in range(len(tl)):
            if i<len(tok):
                lastup = tok[i] in tokens.uppercase # True if the last letter inspected was uppercase
            if lastup:
                tl[i] = tl[i].upper()
        t = ''.join(tl)
	if self.postprocess:
	    t = self.postprocess(t)
        return t

        
if __name__ == '__main__':
    import tables_ludevit
    t = Translate(tables_ludevit.table_voc, tables_ludevit.table_ort, tables_ludevit.postprocess)
#    t = Translate(None, None)
    print `t.trans(u'vláda')`

