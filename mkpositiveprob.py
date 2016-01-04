#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import re

dict = {}
total = 0

for line in codecs.open("positive.txt.chasen","r","euc-jp"):
    line = line.rstrip('\r\n')
    if line == "EOS":
        pass
    else:
        lis = line.split("\t")
        if lis[0] in dict:
            dict[lis[0]] += 1
        else:
            dict[lis[0]] = 1
        total += 1

fp = codecs.open("positive.prob","w","euc-jp")

for x in dict.items():
    prob = x[1]/float(total)
    fp.write(x[0] + "\t" + str(prob) + "\n")

fp.close()
