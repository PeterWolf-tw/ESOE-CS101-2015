#!/usr/bin/env python3
#-*- coding:utf-8 -*-

# 3. 請利用以下空白範本設計一支程式。程式可輸入一段字串，並自動計算出字串中包括空白字元出現的機率。
#    並由高排到低。
def charFreqLister(inputSTR):
#resultLIST = [(freq, char), (freq, char), (freq, char),...]
    LISTa = []
    resultLIST =[]
    n = len(str(inputSTR))
    for i in inputSTR:
        if i not in LISTa:
            LISTa.append((i,str(inputSTR).count(i)/n))
    LISTb = sorted(LISTa, key = lambda x : x[1])
    for i in reversed(LISTb):
        resultLIST.append(i)
    return resultLIST


# 3.1 加分題 (有做有加分，沒做不扣分)：請用課堂中提到的「霍夫曼編碼]
#     (https://zh.wikipedia.org/wiki/霍夫曼編碼) 為你之前設計的
#     程式加上轉碼壓縮的功能。
# e.g.,
#def huffmanTranslater(inputSTR):
#resultLIST = [(freq, char, code), (freq, char, code), (freq, char, code),...]

#return resultLIST


if __name__ == "__main__":
    testSTR01 = "The quick brown fox jumps over the lazy dog"
    result = charFreqLister(testSTR01)
    print(result)
    testSTR02 = "Jim quickly realized that the beautiful gowns are expensive"
    result = charFreqLister(testSTR02)
    print(result)