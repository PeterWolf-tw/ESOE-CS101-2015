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
    #LIST1 = []
    #LIST2 = []
    codeLISTa = []
    codeLISTb = []
    codeLISTj = []
    codeLIST = []
    huffLIST = []

    for a in inputSTR:
        A = inputSTR.count(a)/len(inputSTR)
        LIST1 = []
        if (a, A, codeLISTa) not in LIST1:
            LIST1.append((a, A, codeLISTa))
        LIST1.sort( key = lambda x : x[1], reverse=True)
        for a in inputSTR:
            for b in inputSTR:
                for c in inputSTR:
                    
                    A = inputSTR.count(a)/len(inputSTR)
                    B = inputSTR.count(b)/len(inputSTR)
                    C = inputSTR.count(c)/len(inputSTR)
                    
                #for (a, A, codeLISTa) not in LIST1:
                    #LIST1.append((a, A))
                    #for (b, B, codeLISTb) not in LIST1:
                        #LIST1.append((a, A))
                        #for (c, C, codeLISTc) not in LIST1:
                    if a != b != c:
                        if A<=B<=C<1:
                            K = A + B
                            codeLISTa.append("1")
                            codeLISTb.append("0")
                            A == K
                            B == K
                            #if k <= 1:
                                #for j in inputSTR:
                                    #J = inputSTR.count(j)/len(inputSTR)
                                    
                                    #LIST1.append((j, K, codeLISTj))
                                    #if codeLISTj.append(("1")):
                                        #codeLISTa.append("1")
                                        #codeLISTb.append("1")
                                    #if codeLISTj.append(("0")):
                                        #codeLISTa.append("0")
                                        #codeLISTb.append("0") 
                                
                    return LIST1
    
        if (j, J, codeLISTj) not in huffLIST:
            huffLIST.append((j, J, codeLISTj))        
        huffLIST.sort( key = lambda x : x[1], reverse=True)
    return huffLIST

                
                    
                
                          
                                 

if __name__ == "__main__":
    result1 = charFreqLister(input("give me something:"))
    result2 = huffmanTranslater(input("give me something:"))
    print(result1)
    print(result2)