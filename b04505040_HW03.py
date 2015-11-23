#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def charFreqLister(inputSTR):
        resultLIST = []
        for i in inputSTR
        resultLIST.append((inputSTR.count(i)/len(inputSTR),i))
        
        return resultLIST


if __name__ == "__main__":
    testSTR01 = "The quick brown fox jumps over the lazy dog"
    result = charFreqLister(testSTR)
    print(result)
    testSTR02 = "Jim quickly realized that the beautiful gowns are expensive"
    result = charFreqLister(testSTR)
    print(result)
