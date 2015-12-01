#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def ilovepita(inputSTR):
    resultLIST = []
    
    for x in inputSTR:
        resultLIST.append((inputSTR.count(x)/len(inputSTR),x))
    resultLIST.sort(key=lambda x: x[0] , reverse=True)
    
    return resultLIST



if __name__== "__main__":
    x=input()
    
    print(ilovepita(x))
    