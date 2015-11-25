#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def charFreqLister(inputSTR):
    
    
    a = str(inputSTR)
    b = len(a)
    resultLIST = []
    
    for i in inputSTR:
        r = round(a.count(i)/b,8)
        resultLIST.append((r,i))
       
    f = list(set(resultLIST))
    c = sorted(f)
    return c
d = input("please input a word chain : ")
e = charFreqLister(d)
print(e)


#霍夫曼編碼失敗###############################################################################
#僅有用霍夫曼樹的概念算出機率總和##############################################################
#但是一定是1啊我花那麼多時間幹嘛###############################################################
def huffmantreeprocessor(inputSTR):
    
    a = str(inputSTR)
    b = len(a)
    c = []
        
    for i in inputSTR:
        r = round(a.count(i)/b,8)
        c.append((r))
    d = list(c)
    e = sorted(d)
    
    i = 0
    while i < b-1:
        x = e[0]
        y = e[1]
        f = x + y
        e.append((f))
        del(e[0])
        del(e[0])
        k = sorted(e)
        i = i + 1
    return k
a = input("please input a word chain : ")
b = huffmantreeprocessor(a)
print(b)