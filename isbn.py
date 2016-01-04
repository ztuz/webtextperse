#-*- coding: utf-8 -*-
import re
import codecs

code = raw_input()
# 4873114705 oeilly 自然言語処理入門のisbn番号を使う。
pattern = "^[0-9]{9}[0-9X]{1}$"
if re.match(pattern,code) :
   print "ok match"
else :
   print "not matched"
        
cd = code[-1]
print "cd"
print cd 
data = code[0:-1]
print "data"
print data
total = 0
w = 10
for i in range(0,len(data)):
    total = total + int(data[i]) * w
    w = w - 1
dig = total % 11
dig = 11 - dig
print "dig"
print dig
print "total"
print total
if dig == 10 :
   dig = "X"
   print "dig=x"
if str(dig) == cd :
    print "あってます"
else :
    print "isbnと認識できませんでした。"

