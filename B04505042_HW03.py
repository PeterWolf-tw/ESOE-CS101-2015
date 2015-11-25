#!/usr/bin/env python 3
#-*- coding:utf-8 -*-
def charFreqLister(inputSTR):
    numberofcharacters = len(str(inputSTR))
    result = []    
    for character in inputSTR:
        probability = str(inputSTR). count(character)/numberofcharacters #算出字元或符號的出現機率
        result. append((probability, character)) #加到result裡面
    setofresult = set(result)
    almostresultLIST = list(setofresult)
    resultLIST = sorted(almostresultLIST, reverse = True)
    return resultLIST
##############下面這個是把機率由小排到大的函數,原本想拿來當作霍夫曼編碼的機率list,雖然沒有研究出怎麼做不過還是放上來TAT#############

def probabilityLISTer(inputSTR):
    numberofcharacters = len(str(inputSTR))
    result2 = []    
    for character in inputSTR:
        probability = str(inputSTR). count(character)/numberofcharacters #算出字元或符號的出現機率
        result2. append(probability) #把機率加到result裡面
    resultLIST2 = sorted(result2)
    return resultLIST2#機率


if __name__ == "__main__":
    inputSTR = input("Enter a bunch of words or characters here:")
    t = charFreqLister(inputSTR)
    print(t)
    s = probabilityLISTer(inputSTR)
    print(s)