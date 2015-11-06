#!/usr/bin/env python3
# -*- coding:utf-8 -*-

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
    outputSTR=""
    for i,j in zip(inputSTR_X, inputSTR_Y):
        if i==j==1: outputSTR=outputSTR +"1"
        else: outputSTR=outputSTR +"0"
    return outputSTR

#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    outputSTR=""
    for i,j in zip(inputSTR_X, inputSTR_Y):
        if i==0 and j==0: outputSTR=outputSTR +"0"
        else: outputSTR=outputSTR +"1"
    return outputSTR

#condition00 xor condition04
def condXOR(inputSTR_X, inputSTR_Y):
    outputSTR=""
    for i,j in zip(inputSTR_X, inputSTR_Y):
        if i==j: outputSTR=outputSTR +"0"
        else: outputSTR=outputSTR +"1"
    return outputSTR



def hex2Bin(hexSTR):
    '''
    16 進位表示式轉為 2 進位表示式
    '''
    return bin(int(hexSTR, 16))[2:]


if __name__== "__main__":
    condition00X = "010111001010100001100011"
    condition00Y = "010000110001011100101001"

    condition01 = condNOT(condition00X)
    print(condition01)
    condition02 = condAND(condition00X,condition00Y)                            
    print(condition02)
    condition03 = condOR(condition00X,condition00Y)
    print(condition03)
    condition04 = condXOR(condition00X,condition00Y)
    print(condition04)    

    #可利用 hex2Bin() 函式計算十六進位表示式 "99" 的二進位表式：(範例如下)
    b = hex2Bin("99")
    print(b)


    print("Ans:")
    print("Ch4P4_3a = \"10011001\"")
    print("Ch4P4_3b = \"11111111\"")
    print("Ch4P4_3c = \"10011001\"")
    print("Ch4P4_3d = \"11111111\"")
    print("========")
    print("Ch4P4_4a = \"01100110\"")
    print("Ch4P4_4b = \"11111111\"")
    print("Ch4P4_4c = \"00010001\"")
    print("Ch4P4_4d = \"10111011\"")
    print("========")
    print("Ch4P4_13a = \"1184\"")
    print("Ch4P4_13b = \"-862\"")
    print("Ch4P4_13c = \"862\"")
    print("Ch4P4_13d = \"-1184\"")
    print("========")
    print("Ch4P4_15a = \"overflow\"")
    print("Ch4P4_15b = \"-73\"")
    print("Ch4P4_15c = \"73\"")
    print("Ch4P4_15d = \"overflow\"")
    print("========")
    print("Ch4P4_16a = \"0F51\"")
    print("Ch4P4_16b = \"OF2A\"")
    print("Ch4P4_16c = \"8012\"")
    print("Ch4P4_16d = \"7F51\"")