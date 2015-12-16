#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from __future__ import division

def charFreqLister(inputSTR):
    a = len(inputSTR)
    freq = {}
    letterlist = []
    for letter in inputSTR:
        freq[letter] = inputSTR.count(letter)/a
    for letter in freq:
        letterlist.append((freq[letter],letter))
    letterlist.sort(reverse=True)
    return letterlist

def huffman(inputSTR):
    letterlist=[]
    freqlist=[]
    mainlist=[]
    resultlist=[]
    for i in inputSTR:
        if i not in letterlist:
            letterlist.append(i)
            freqlist.append(inputSTR.count(i)/len(inputSTR))
    for i in range(0, len(letterlist)):
        mainlist.append((freqlist[i], letterlist[i]))

    for i in range(0, len(mainlist)-1):
        mainlist.sort(reverse=False)
        if len(mainlist[0][1]) == 1:
            resultlist.append([mainlist[0][0], mainlist[0][1], "0"])
        else:
            for i in mainlist[0][1]:
                for j in range(0, len(resultlist)):
                    if i == resultlist[j][1]:
                        resultlist[j][2] = "0" + resultlist[j][2]
        if len(mainlist[1][1]) == 1:
            resultlist.append([mainlist[1][0], mainlist[1][1], "1"])
        else:
            for i in mainlist[1][1]:
                for j in range(0, len(resultlist)):
                    if i == resultlist[j][1]:
                        resultlist[j][2] = "1" + resultlist[j][2]
        mainlist[0]=(mainlist[0][0]+mainlist[1][0], mainlist[0][1]+mainlist[1][1])
        mainlist.remove(mainlist[1])
    resultlist.sort(reverse=True)
    return resultlist
    
        
    

if __name__ == "__main__":
    testSTR01 = "The quick brown fox jumps over the lazy dog"
    result = charFreqLister(testSTR01)
    print(result)
    testSTR02 = "Jim quickly realized that the beautiful gowns are expensive"
    result = charFreqLister(testSTR02)
    print(result)
    result = huffman(testSTR01)
    print(result)
    result = huffman(testSTR02)
    print(result)
