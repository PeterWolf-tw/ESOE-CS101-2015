#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def charFreqLister(inputSTR):
    n = len(inputSTR)
    m = float(n)
    resultLIST = []
    for i in inputSTR:
        j = inputSTR.count(i)/m
        if (j,i) not in resultLIST:
            resultLIST.append((j,i))
            resultLIST.sort()
            resultLIST.reverse()
    
    return resultLIST

if __name__ == "__main__":
    inputSTR  = 'nqofkn1no nkF cDKLF csDK c;c;fef'
    print(charFreqLister(inputSTR))