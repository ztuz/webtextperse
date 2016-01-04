#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import re

dict = {}

for line in codecs.open("okashira.txt.chasen","r","EUC-jp"):
    line = line.rstrip('\r\n')
    if line == "EOS":
        pass
    else:
        lis = line.split("\t")
        
        if re.search(ur'名詞',lis[3]):
           if lis[0]  in dict:
                dict[lis[0]] += 1
           else:
                dict[lis[0]] = 1  

for x in sorted(dict.items(), key=lambda x:x[1], reverse=True):
    print x[0]

