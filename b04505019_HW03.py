#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def charFreqLister(inputSTR):
    
    
    a = str(inputSTR)
    b = len(a)
    resultLIST = []
    
    for i in inputSTR:
        r = round(a.count(i)/b,16)
        resultLIST.append((i,r))
       
    f = list(set(resultLIST))
    c = sorted(f)
    return c
d = input("please input a word chain : ")
e = charFreqLister(d)
print(e)