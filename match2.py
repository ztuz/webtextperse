#!/usr/bin/python
#-*- coding: utf-8 -*-
import re

for line in open("country_names.lst","r"):
  line = line.rstrip()
  if re.search(r"^tan",line,re.IGNORECASE) or re.search(r"tan$",line,re.IGNORECASE):
    print line
