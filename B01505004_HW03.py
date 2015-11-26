#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def charFreqLister(inputSTR):
    resultLIST = []
    
    
    for i in inputSTR:
        if (inputSTR.count(i)/len(inputSTR),i) in resultLIST:
            zip
        else:
            resultLIST.append((inputSTR.count(i)/len(inputSTR),i))
    resultLIST.sort(reverse=True)

    return resultLIST

if __name__== "__main__":
    print(charFreqLister(input("please enter simething:")))
