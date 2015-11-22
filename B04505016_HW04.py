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
    for (i, j) in zip(inputSTR_X, inputSTR_Y):
        if a + b == '1':
            outputSTR = outputSTR + '1'
        else:
            outputSTR = outputSTR + '0'
    return outputSTR

#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for (i, j) in zip(inputSTR_X, intputSTR_Y):
        if a and b == '0':
            outputSTR += '0'
        else:
            outputSTR += '1'
    return outputSTR

#condition00 xor condition04
def conXOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for (i, j) in zip(inputSTR_X, inputSTR_Y):
        if a == b:
            outputSTR += '0'
        else:
            outputSTR += '1'
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
    
    
       #print("Ans:")
       #Ch4P4_3a = ""
       #Ch4P4_3b = ""
       #Ch4P4_3c = ""
       #Ch4P4_3d = ""
       #print("========")
       #Ch4P4_4a = ""
       #Ch4P4_4b = ""
       #Ch4P4_4c = ""
       #Ch4P4_4d = ""
       #print("========")
       #Ch4P4_13a = ""
       #Ch4P4_13b = ""
       #Ch4P4_13c = ""
       #Ch4P4_13d = ""
       #print("========")
       #Ch4P4_15a = ""
       #Ch4P4_15b = ""
       #Ch4P4_15c = ""
       #Ch4P4_15d = ""
       #print("========")
       #Ch4P4_16a = ""
       #Ch4P4_16b = ""
       #Ch4P4_16c = ""
       #Ch4P4_16d = ""    