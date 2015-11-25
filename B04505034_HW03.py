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



    for i in inputSTR:
        I = inputSTR.count(i)
        if (i,I/len(inputSTR)) not in resultLIST:
            resultLIST.append((i,I/len(inputSTR)))
    resultLIST.sort( key = lambda x : x[1], reverse=True)
    
    return resultLIST


# 3.1 加分題 (有做有加分，沒做不扣分)：請用課堂中提到的「霍夫曼編碼]
#     (https://zh.wikipedia.org/wiki/霍夫曼編碼) 為你之前設計的
#     程式加上轉碼壓縮的功能。
# e.g.,
def huffmanTranslater(inputSTR):
    huffLIST = []
    LIST = []
    codeLISTa = []
    codeLISTb = []

    for a in inputSTR:
        A = inputSTR.count(a)/len(inputSTR)
        for b in inputSTR:
            B = inputSTR.count(b)/len(inputSTR)
            for c in inputSTR:              
                C = inputSTR.count(c)/len(inputSTR)
                for (a, A, codeLISTa) in LIST:
                    for (b, B, codeLISTb) in LIST:
                        for (c, C, codeLISTc) in LIST:
                            if A<=B<=C<1:
                                K = A + B
                                codeLISTa.append("1")
                                codeLISTb.append("0")
                            return LIST.append(a, A==K, codeLISTa), LIST.append(b, B==K, codeLISTb)
                
                    
                
                          
    if (a, A, codeLISTa) not in huffLIST:
        huffLIST.append(a, A, codeLISTa)
    
    if (b, B, codeLISTb) not in huffLIST:
        huffLIST.append(b, B, codeLISTb) 
    
                   
                
                                       
    
    huffLIST.sort( key = lambda x : x[1], reverse=True)
                
            
                
            
    return huffLIST


if __name__ == "__main__":
    result1 = charFreqLister(input("give me something:"))
    result2 = huffmanTranslater(input("give me something:"))
    print(result1)
    print(result2)