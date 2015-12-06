# !/usr/bin/env python3
#  -*- coding:utf-8 -*-

def charFreqLister(inputLIST):

    
    n = len(inputLIST)
    result = []

    for i in inputLIST:
        j = float('%.3f'%(inputLIST.count(i)/n))
        result.append((i,j))
    resultLIST = list(set(result))
    resultLIST.sort(key=lambda tup: tup[1], reverse=True)
    
    return resultLIST    
    
inputLIST = input("Please insert something: ")   

print(charFreqLister(inputLIST))