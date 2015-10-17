#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#Python 程式的前兩行是固定的，請牢記。

#A beautiful solution!
tmp=input()
sum=0
for i in range(len(tmp)):
	sum+= 2**i*int(tmp[-(i+1)])
#Python 的縮排請用四個空格。

print(sum)

#其它題目和答案呢？