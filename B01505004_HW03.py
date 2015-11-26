#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def charFreqLister(inputSTR):
    resultLIST = []
    
    
    for n in inputSTR:
        if (inputSTR.count(n)/len(inputSTR),n) in resultLIST:
            zip
        else:
            resultLIST.append((inputSTR.count(n)/len(inputSTR),n))
    resultLIST.sort(reverse=True)

    return resultLIST

if __name__== "__main__":
    print(charFreqLister(input("please enter simething:")))
