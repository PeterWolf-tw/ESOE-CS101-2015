#!/usr/bin/env python3
#-*- coding:utf-8 -*-

# 3. 請利用以下空白範本設計一支程式。程式可輸入一段字串，並自動計算出字串中包括空白字元出現的機率。
# 並由高排到低。

#resultLIST = [(freq, char), (freq, char), (freq, char),...]
def charFreqLister(inputSTR):
    resultLIST = []
    n = len(inputSTR)

    for i in inputSTR:
        a = inputSTR.count(i)    
        if (i, a/n) not in resultLIST:
            resultLIST.append(i, a/n)
            resultLIST.sort(reverse = True)

    return resultLIST

if "_name_" == "_main_":
    print(charFreqLister(input("Please type something")))