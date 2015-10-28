#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#請參考以下 condNOT() 的例子，設計四個 func() 依以下條件，能算出 condition02 ~ 04 的值

#condition00 not condition01
def condNOT(inputSTR_X):
    outputSTR = ""
    for i in inputSTR_X:
        if i == "0":
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
    return outputSTR


#condition00 and condition02
def condAND(inputSTR_X, inputSTR_Y):
    outputSTR = ""    
    i = 0
    j = 0
    
    while(i < len(inputSTR_X)):
        if(int(inputSTR_X[i]) == int(inputSTR_Y[j])):        
            outputSTR = outputSTR + inputSTR_X[i]
        else:
            outputSTR = outputSTR + "0"
        i += 1
        j += 1
    return outputSTR

#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    
    i = 0
    j = 0
    
    while(i < len(inputSTR_X)):
        if(int(inputSTR_X[i]) == 1 or int(inputSTR_Y[j]) == 1):        
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
        i += 1
        j += 1
    return outputSTR

#condition00 xor condition04
def conXOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    
    i = 0
    j = 0
    
    while(i < len(inputSTR_X)):
        if(int(inputSTR_X[i]) == int(inputSTR_Y[j])):        
            outputSTR = outputSTR + "0"
        else:
            outputSTR = outputSTR + "1"
        i += 1
        j += 1
    return outputSTR
