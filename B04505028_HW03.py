#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def charFreqLister(inputSTR):
    resultList=[]
    L=len(inputSTR)
    for i in inputSTR:
        X=str(inputSTR).count(i)/L
        if (X,i) not in resultList:
            resultList.append((X,i))
    resultList=list(resultList)
    resultList.sort(reverse=True)
    return resultList

def order(TPA):
    facList=charFreqLister(TPA)
    facLen=len(facList)
    freqListforcode=[]
    charListforcode=[]
    freqList2forcode={}
    for i in facList:
        freqListforcode.append(i[0])
        charListforcode.append(i[1])
        freqList2forcode[i[1]] = i[0]
    nList2={}
    i = 1
    while i < facLen :
        freqList=[]
        charList=[]        
        for h in facList:
            freqList.append(h[0]) 
            charList.append(h[1])  
        n = [charList[-2],charList[-1]]
        nList2[i] = n
        f = freqList[-2] + freqList[-1]
        del freqList[-2]
        del freqList[-1]
        del charList[-2]
        del charList[-1]     
        facList=[]
        for j in range(len(freqList)):
            facList.append([freqList[j],charList[j]])
        facList.append([f,n])
        facList.sort(key= lambda x : x[0] ,reverse=True)
        i += 1   
    resultList2={}
    for i in charListforcode:
        resultList2[i] = ""
    for i in range(1,facLen):
        a = nList2[i]
        for k in charListforcode:
            if k in str(a[0]).replace(", ",","): 
                resultList2[k] = "1" + resultList2[k]
            if k in str(a[1]).replace(", ",","):
                resultList2[k] = "0" + resultList2[k]
    resultList=[]
    for i in charListforcode:
        if i in resultList2:
            resultList.append([freqList2forcode[i],i,resultList2[i]])

    return resultList
if __name__ == "__main__":
    T=charFreqLister(input("enter something:"))
    print (T)
    D=order(input("enter something:"))   
    print (D)       