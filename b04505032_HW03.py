#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#狂 yee



def charFreqLister(inputSTR):
    resultLIST = []
    


    
    for i in inputSTR:
        c = inputSTR.count(i)
        if (i,c/len(inputSTR)) not in resultLIST:
            resultLIST.append((i,c/len(inputSTR)))
    resultLIST.sort( key = lambda x : x[1])
        
    return resultLIST