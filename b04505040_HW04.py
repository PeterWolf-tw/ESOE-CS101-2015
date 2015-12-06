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
    outputSTR = ""
    for a,b in zip(inputSTR_X, inputSTR_Y):
        if a and b =="1":
             outputSTR = outputSTR + "1" #每次縮排是四個空格。你這裡多了一個空格。
        else:
             outputSTR = outputSTR + "0" #每次縮排是四個空格。你這裡多了一個空格。

    return outputSTR

#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    outputSTR = "" #這裡要先實體化一個 outputSTR，之後才能用來操作。
    for a,b in zip(inputSTR_X, inputSTR_Y):
        if a and b =="0":
             outputSTR = outputSTR + "0" #每次縮排是四個空格。你這裡多了一個空格。
        else:
             outputSTR = outputSTR + "1" #每次縮排是四個空格。你這裡多了一個空格。
    return outputSTR

#condition00 xor condition04
def condXOR(inputSTR_X, inputSTR_Y):
    outputSTR = "" #這裡要先實體化一個 outputSTR，之後才能用來操作。
    for a,b in zip(inputSTR_X, inputSTR_Y):
        if a == b:
             outputSTR = outputSTR + "0" #每次縮排是四個空格。你這裡多了一個空格。
        else:
             outputSTR = outputSTR + "1" #每次縮排是四個空格。你這裡多了一個空格。
    return  outputSTR



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
    condition02=condAND(condition00X,condition00Y)
    print(condition02)
    condition03=condOR(condition00X,condition00Y)
    print(condition03)
    condition04=condXOR(condition00X,condition00Y)
    print(condition03)




    print("Ans:")
    Ch4P4_3a = "10011001"
    Ch4P4_3b = "11111111"
    Ch4P4_3c = "10011001"
    Ch4P4_3d = "11111111"
    print("========")
    Ch4P4_4a = "01100110"
    Ch4P4_4b = "11111111"
    Ch4P4_4c = "00010001"
    Ch4P4_4d = "10111011"
    print("========")
    Ch4P4_13a = "1184"
    Ch4P4_13b = "-862"
    Ch4P4_13c = "862"
    Ch4P4_13d = "-1184"
    print("========")
    Ch4P4_15a = "overflow"
    Ch4P4_15b = "not overflow" #-73
    Ch4P4_15c = "not overflow" #73
    Ch4P4_15d = "overflow"
    print("========")
    Ch4P4_16a = "0F51"
    Ch4P4_16b = "0F2A"
    Ch4P4_16c = "8012"
    Ch4P4_16d = "7F51"
