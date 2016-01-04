#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#請參考 http://interactivepython.org/runestone/static/pythonds/SortSearch/sorting.html
#中提供的 bubble sorting 演算法，將整數列表 [5, 16, 20, 3, 8, 12, 9, 17, 20, 7] 由大排到小。

def bubble(n):
    inputLIST=n 
    outputLIST=[]
    while len(inputLIST)!=0:
        outputLIST.append(max(inputLIST))
        inputLIST.remove(max(inputLIST))
    return outputLIST


if __name__== "__main__":
    q=[5, 16, 20, 3, 8, 12, 9, 17, 20, 7]
    print(bubble(q))