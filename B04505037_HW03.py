# !/usr/bin/env python3
#  -*- coding:utf-8 -*-

def charFreqLister(x):

    
    n = len(str(x))
    result = []

    for i in x:
        j = float('%.3f'%(str(x).count(i)/n))
        result.append((j,i))
    resultLIST = list(set(result))
    resultLIST.sort(reverse=True)
    return resultLIST    
    
x = input("Please insert something: ")   
k = charFreqLister(x)
print(k)