#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def charFreqLister(inputSTR):
    
    x = str(inputSTR)
    L = len(x)
    resultLIST = []
    
    for i in inputSTR:
        R = round( x.count(i) / L,8 )
        resultLIST.append((R,i))
       
    a = list(set(resultLIST))
    S = sorted(a)
    return S

if __name__ == "__main__":
    y = input("please input a word chain : ")
    z = charFreqLister(y)
    print(z)
