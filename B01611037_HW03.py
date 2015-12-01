#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 繳交日期：2015.11.26

# 作業內容：
# 1. 請參閱 Wikipedia 維基百科 IEEE754 條目 (https://zh.wikipedia.org/wiki/IEEE_754)
# 此題不用繳交，期中/期未考試自然見真章。

# 2. 請試玩 http://armorgames.com/play/17826/logical-element

# 3. 請利用以下空白範本設計一支程式。程式可輸入一段字串，並自動計算出字串中包括空白字元出現的機率。
#    並由高排到低。
def charFreqLister(inputSTR):
    resultLIST = []
    
    
    for n in inputSTR:
        if (inputSTR.count(n)/len(inputSTR),n) in resultLIST:
            zip
        else:
            resultLIST.append((inputSTR.count(n)/len(inputSTR),n))
    resultLIST.sort(reverse=True)

    return resultLIST

if __name__== "__main__":
    print(charFreqLister(input("please enter simething:")))
