#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from __future__ import division 
#使/從classic division 變成true division
#classic division: 1/2 ≠ 1.0/2.0  = 0 , 5/3  = 1
#true division:    1/2 = 1.0/2.0      , 5/3  = 1.66666666667
#floor division:  1//2 = 1.0//2.0 = 0 , 5//3 = 1 

def charFreqLister(inputSTR):
    
    resultLIST = []
    a = []
    for i in inputSTR:
        if i not in a:
            resultLIST.append([inputSTR.count(i)/len(inputSTR),i])
            a.append(i)    
    resultLIST.sort(reverse = True)   #True的T要大寫

    return resultLIST


# 3.1 加分題 (有做有加分，沒做不扣分)：請用課堂中提到的「霍夫曼編碼]
#     (https://zh.wikipedia.org/wiki/霍夫曼編碼) 為你之前設計的
#     程式加上轉碼壓縮的功能。
# e.g.,
def huffmanTranslater(inputSTR): 
    
    facLIST = charFreqLister(inputSTR)
    facLEN = len(facLIST)
    freqLIST = []
    copycharLIST = []
    for i in facLIST:
        copycharLIST.append(i[1]) 
    fDICT = {}
    nDICT = {}
    i = 1
    while i < facLEN :
        freqLIST = []
        charLIST = []        
        for h in facLIST:
            freqLIST.append(h[0]) 
            charLIST.append(h[1])  
        n = [charLIST[-2],charLIST[-1]]
        nDICT[i] = n
        f = freqLIST[-2] + freqLIST[-1]
        del freqLIST[-2]
        del freqLIST[-1]
        del charLIST[-2]
        del charLIST[-1]     
        facLIST = []
        for j in range(len(freqLIST)):
            facLIST.append([freqLIST[j],charLIST[j]])
        facLIST.append([f,n])
        facLIST.sort(key= lambda x : x[0] ,reverse=True)
        i += 1
    #print("i=",i," fDICT=",fDICT)
    #print("i=",i," nDICT=",nDICT)
    #print("i=",i," facLIST=",facLIST)    
    resultDICT = {}
    for i in copycharLIST:
        resultDICT[i] = ""
    for i in range(1,facLEN):
        for k in copycharLIST:
            a = nDICT[i]
            if  k in str(a[0]).replace(", ",","): 
                resultDICT[k] = "1" + resultDICT[k]
            if  k in str(a[1]).replace(", ",","):
                resultDICT[k] = "0" + resultDICT[k]  
                
    return resultDICT
    

    #resultLIST = [(freq, char, code)]
    #return resultLIST

if __name__== "__main__":
    testSTR01 = "The quick brown fox jumps over the lazy dog"
    result = charFreqLister(testSTR01)
    print(result)
    testSTR02 = "Jim quickly realized that the beautiful gowns are expensive"
    result = charFreqLister(testSTR02)
    print(result)
    result = huffmanTranslater(testSTR01)
    print(result)    
    result = huffmanTranslater(testSTR02)
    print(result)
    a = "abbccc"
    result = charFreqLister(a)
    print(result)
    result = huffmanTranslater(a)
    print(result)