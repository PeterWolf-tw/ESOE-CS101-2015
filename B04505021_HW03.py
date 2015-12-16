#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 繳交日期：2015.11.26

# 作業內容：
# 1. 請參閱 Wikipedia 維基百科 IEEE754 條目 (https://zh.wikipedia.org/wiki/IEEE_754)
# 此題不用繳交，期中/期未考試自然見真章。

#done

# 2. 請試玩 http://armorgames.com/play/17826/logical-element

#done

# 3. 請利用以下空白範本設計一支程式。程式可輸入一段字串，並自動計算出字串中包括空白字元出現的機率。
#    並由高排到低。
def charFreqLister(inputSTR):

    charList = []
    frequencyList = []
    resultLIST = []
    for i in inputSTR :
        if i not in charList:
            charList.append(i)
            frequencyList.append(inputSTR.count(i)/len(inputSTR) )
    for i in range (0,len(charList)):
        resultLIST.append((frequencyList[i] , charList[i]))
        
    resultLIST.sort(reverse=True)
    
    return resultLIST


# 3.1 加分題 (有做有加分，沒做不扣分)：請用課堂中提到的「霍夫曼編碼]
#     (https://zh.wikipedia.org/wiki/霍夫曼編碼) 為你之前設計的
#     程式加上轉碼壓縮的功能。
# e.g.,
def huffmanTranslater(inputSTR):
    resultLIST = []
    charList = []
    frequencyList = []
    LIST = []
    for i in inputSTR :
        if i not in charList:
            charList.append(i)
            frequencyList.append(inputSTR.count(i)/len(inputSTR) )
    for i in range (0,len(charList)):
        LIST.append((frequencyList[i] , charList[i]))
        
    for i in range (0,len(LIST)-1) :
        LIST.sort(reverse=False)
        if len(LIST[0][1]) == 1 :
            resultLIST.append ([LIST[0][0],LIST[0][1] ,"0"])
        else :
            for i in LIST[0][1]:
                for j in range(0,len(resultLIST)):
                    if i == resultLIST[j][1]:
                        resultLIST[j][2] = "0" + resultLIST[j][2]
        if len(LIST[1][1]) == 1 :
            resultLIST.append ([LIST[1][0],LIST[1][1] ,"1"])
        else :
            for i in LIST[1][1]:
                for j in range(0,len(resultLIST)):
                    if i == resultLIST[j][1]:
                        resultLIST[j][2] = "1" + resultLIST[j][2]
        LIST[0]=(LIST[0][0]+LIST[1][0],LIST[0][1]+LIST[1][1])
        LIST.remove(LIST[1])
    resultLIST.sort(reverse=True)
    return resultLIST


if __name__ == "__main__":
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