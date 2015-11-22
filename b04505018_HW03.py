#!/usr/bin/env python3
# -*- coding:utf-8 -*-



def charFreqLister(inputSTR):

    resultLIST=[]

    for y in inputSTR :
        x=[inputSTR.count(y)/float(len(inputSTR))]#字母出現次數除以總長。為避免 int/int 時最小為 0 。加上 float() 以便讓 len(inputSTR)成為一個浮點數。
        resultLIST.append((x,y))
    return resultLIST

if __name__== "__main__":
    print(charFreqLister("this is a short test."))