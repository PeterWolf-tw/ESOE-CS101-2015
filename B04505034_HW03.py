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
    freq = []
    a = []
    
    for i in inputSTR:
        if i not in a:
            a.append(i)



    for i in inputSTR:
        I = inputSTR.count(i)
        if (I/len(inputSTR), i) not in resultLIST:
            resultLIST.append((I/len(inputSTR), i))
    resultLIST.sort( reverse=True)
    
    return resultLIST


# 3.1 加分題 (有做有加分，沒做不扣分)：請用課堂中提到的「霍夫曼編碼]
#     (https://zh.wikipedia.org/wiki/霍夫曼編碼) 為你之前設計的
#     程式加上轉碼壓縮的功能。
# e.g.,
def huffmanTranslater(inputSTR):
    
    facLIST = charFreqLister(inputSTR)
    facLEN = len(facLIST)
    freqLISTforcode = []
    charLISTforcode = []
    freqDICTforcode = {}
    for i in facLIST:
        freqLISTforcode.append(i[0])
        charLISTforcode.append(i[1])
        freqDICTforcode[i[1]] = i[0]
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
    #print("i=",i," nDICT=",nDICT)
    #print("i=",i," facLIST=",facLIST)    
    resultDICT = {}
    for i in charLISTforcode:
        resultDICT[i] = ""
    for i in range(1,facLEN):
        a = nDICT[i]
        for k in charLISTforcode:
            if k in str(a[0]).replace(", ",","): 
                resultDICT[k] = "1" + resultDICT[k]
            if k in str(a[1]).replace(", ",","):
                resultDICT[k] = "0" + resultDICT[k]
    resultLIST = []
    for i in charLISTforcode:
        if i in resultDICT:
            resultLIST.append([freqDICTforcode[i],i,resultDICT[i]])

    return resultLIST

                
                    
                
                          
                                 

if __name__ == "__main__":
    result1 = charFreqLister(input("give me something:"))
    print(result1)
    result2 = huffmanTranslater(input("give me something:"))
    
    print(result2)