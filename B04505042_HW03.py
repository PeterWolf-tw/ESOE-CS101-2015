#!/usr/bin/env python 3
#-*- coding:utf-8 -*-
def charFreqLister(inputSTR):
    numberofcharacters = len(str(inputSTR))
    result = []    
    for character in inputSTR:
        probability = str(inputSTR). count(character)/numberofcharacters #算出字元或符號的出現機率
        result. append((probability, character)) #加到result裡面
    setofresult = set(result)
    almostresultLIST = list(setofresult)
    resultLIST = sorted(almostresultLIST, reverse = True)
    return resultLIST


if __name__ == "__main__":
    inputSTR = input("Enter a bunch of words or characters here:")
    t = charFreqLister(inputSTR)
    print(t)
    n = -1
    for a in t:
        print(a[0])
    