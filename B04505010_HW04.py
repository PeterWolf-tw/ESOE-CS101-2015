#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def condNOT(inputSTR_X):
    outputSTR = ""  
    for i in inputSTR_X:
        if i == "0":
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
    return outputSTR

def condAND(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    x=str(inputSTR_X)
    y=str(inputSTR_Y)
    L=len(x)
    for i in range(0,L):
        if x[i]=="1" and y[i]=="1" :
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
    return outputSTR

def condOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    x=str(inputSTR_X)
    y=str(inputSTR_Y)
    L=len(x)
    for i in range(0,L):
        if x[i]=="1" or y[i]=="1" :
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
    return outputSTR

def condXOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    x=str(inputSTR_X)
    y=str(inputSTR_Y)
    L=len(x)
    for i in range(0,L):
        if x[i]=="1" or y[i]=="1" :
            if x[i]=="1" and y[i]=="1":
                outputSTR = outputSTR + "0"
            else:
                outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
    return outputSTR

if __name__== "__main__":
    condition00X = "010111001010100001100011"
    condition00Y = "010000110001011100101001"

    condition01 = condNOT(condition00X)
    print(condition01)    
    
    condition02 = condAND(condition00X, condition00Y)
    print(condition02)
    
    condition03 = condOR(condition00X, condition00Y)
    print(condition03)
    
    condition04 = condXOR(condition00X, condition00Y)
    print(condition04)