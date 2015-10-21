#!/usr/bin/env python3
#-*- coding:utf-8 -*-

def charFreqLister(inputSTR):
    str=inputSTR[0]
    sum=len(inputSTR)
    for i in range(1,sum):
        repeat=0
        for j in str:
            if inputSTR[i]==j :
                repeat=1
                break
        if repeat==0:  str=str+inputSTR[i]
    resultLIST=[[0.25,'b'] for j in range(len(str))]
    for i in range(len(str)):
        resultLIST[i][0]=round(inputSTR.count(str[i])/sum,2)
        resultLIST[i][1]=str[i]
    temp=[0.1,'b']
    for i in range(len(str)):
        for j in range(len(str)-i-1):
            if(resultLIST[j][1]>resultLIST[j+1][1]):
                temp=resultLIST[j]
                resultLIST[j]=resultLIST[j+1]
                resultLIST[j+1]=temp
    return resultLIST
if __name__ == '__main__': 
    print("Please input a string:")
    LIST=charFreqLister(input())
    print (LIST)
  
    
    
    
# 3.1 加分題 (有做有加分，沒做不扣分)：請用課堂中提到的「霍夫曼編碼]
#     (https://zh.wikipedia.org/wiki/霍夫曼編碼) 為你之前設計的
#     程式加上轉碼壓縮的功能。
#def huffmanTranslater(inputSTR):
#resultLIST = [(freq, char, code), (freq, char, code), (freq, char, code),...]
    
#return resultLIST    