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
    for i,j in zip(inputSTR_X,inputSTR_Y):
        if i == j == "1":
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
    return outputSTR

#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for i,j in zip(inputSTR_X, inputSTR_Y):
        if i == j == "0":
            outputSTR = outputSTR + "0"
        else:
            outputSTR = outputSTR + "1"
    return outputSTR

#condition00 xor condition04
def condXOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for i,j in zip(inputSTR_X, inputSTR_Y):
        if i == j:
            outputSTR = outputSTR + "0"
        else:
            outputSTR = outputSTR + "1"
    return outputSTR



    
if __name__== "__main__":
    condition00X = "010111001010100001100011"
    condition00Y = "010000110001011100101001"
    
    condition02 = condAND(condition00X,condition00Y)
    print(condition02)    
    condition03 = condOR(condition00X,condition00Y)
    print(condition03)    
    condition04 = condXOR(condition00X,condition00Y)
    print(condition04)
    
    #Ch4P4_3a = "10011001"
    #Ch4P4_3b = "11111111"
    #Ch4P4_3c = "10011001"
    #Ch4P4_3d = "11111111"

    #Ch4P4_4a = "01100110"
    #Ch4P4_4b = "11111111"
    #Ch4P4_4c = "00010001"
    #Ch4P4_4d = "10111011"
    
    #Ch4P4_13a = "1184"
    #Ch4P4_13b = "-862"
    #Ch4P4_13c = "862"
    #Ch4P4_13d = "-1184"
    
    #Ch4P4_15a = "overflow"
    #Ch4P4_15b = "will not overflow"
    #Ch4P4_15c = "will not overflow"
    #Ch4P4_15d = "overflow"
    
    #Ch4P4_16a = "0F51"
    #Ch4P4_16b = "0F2A"
    #Ch4P4_16c = "8012"
    #Ch4P4_16d = "7F51"  