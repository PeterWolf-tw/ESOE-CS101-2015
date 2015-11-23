#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def charFreqLister(inputSTR):
    inputSTR_1 = inputSTR.join(sorted(key=lambda x: x.lower()))
    letterLIST = []
    resultLIST = []
    charFreqDICT = {}
    charCodeDICT = {}
    SpaceLen = len(inputSTR) - len(inputSTR.replace(' ', ''))
    inputSTR = inputSTR.replace(' ', '')
    x = len(inputSTR) + SpaceLen
    
    #將去除Space後的inputSTR_1帶入
    n = 0     
    while len(inputSTR) > 0:
        letterLen = inputSTR.count(inputSTR[0])
        letterFreq = 1.0*letterLen/x
        charFreqDICT[inputSTR[0]]=letterFreq
        letterLIST.append(inputSTR[0])
        inputSTR = inputSTR.strip(inputSTR[0])
        n += 1
    #letterLen為字母數，每讀完一字即將重複字元拿掉，並計算出現頻率。
    #將字母及頻率放進charFreqDICT
   
    if SpaceLen != 0:
        letterLIST.append(" ")
        charFreqDICT[" "] = 1.0*SpaceLen/x
    #將空白字元一併填入
    
    sorted(charFreqDICT,reverse = True)
    for i in letterLIST:
        resultLIST.append((i,charFreqDICT[i]))
    return resultLIST

if __name__ == "__main__":
    testSTR = "abbccc    "
    print(charFreqLister(testSTR))
