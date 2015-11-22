#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 繳交日期：2015.11.26

# 作業內容：
# 1. 請參閱 Wikipedia 維基百科 IEEE754 條目 (https://zh.wikipedia.org/wiki/IEEE_754)
# 此題不用繳交，期中/期未考試自然見真章。

# 2. 請試玩 http://armorgames.com/play/17826/logical-element

# 3. 請利用以下空白範本設計一支程式。程式可輸入一段字串，並自動計算出字串中包括空白字元出現的機率。
#    並由高排到低。
#def charFreqLister(inputSTR):
#resultLIST = [(freq, char), (freq, char), (freq, char),...]

#return resultLIST


# 3.1 加分題 (有做有加分，沒做不扣分)：請用課堂中提到的「霍夫曼編碼]
#     (https://zh.wikipedia.org/wiki/霍夫曼編碼) 為你之前設計的
#     程式加上轉碼壓縮的功能。
# e.g.,
#def huffmanTranslater(inputSTR):
#resultLIST = [(freq, char, code), (freq, char, code), (freq, char, code),...]

#return resultLIST

def charFreqLister (str1):
    storeidx=[0]
    storechar=['a']
    ls=len(str1)
    storechar[0]=str1[0]
    storeidx[0]=0
    #count--
    for idx in range(len(str1)):
        check=False
        for jdx in range (len(storechar)):
            if storechar[jdx]==str1[idx]:
                storeidx[jdx]+=1
                check=True
        if check==False:
            storechar.append(str1[idx])
            storeidx.append(1)
    #sort--
    for i in range(len(storechar)):
        for j in range(i):
            if storeidx[i]>=storeidx[j]:
                tempidx=storeidx[i]
                tempjdx=storeidx[j]
                tempchari=storechar[i]
                tempcharj=storechar[j]
                storeidx[i]=tempjdx
                storeidx[j]=tempidx
                storechar[i]=tempcharj
                storechar[j]=tempchari
    #print--
    result=[]
    for i in range(len(storechar)):
        cnum=round(storeidx[i]*100.0/ls,2)
        result.append("("+str(cnum)+"%, "+storechar[i]+")")
    return result
    

if __name__ == "__main__":
    testSTR01 = "The quick brown fox jumps over the lazy dog"
    result = charFreqLister(testSTR01)
    print(result)
    testSTR02 = "Jim quickly realized that the beautiful gowns are expensive"
    result = charFreqLister(testSTR02)
    print(result)


                
        

















    
