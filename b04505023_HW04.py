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
    j = 0
    for i in inputSTR_X:
        if i == "1" and inputSTR_Y[j] == "1":
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
        j += 1
    return outputSTR

#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    j = 0
    for i in inputSTR_X:
        if i == "0" and inputSTR_Y[j] == "0":
            outputSTR = outputSTR + "0"
        else:
            outputSTR = outputSTR + "1"
        j += 1
    return outputSTR

#condition00 xor condition04
def conXOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    j = 0
    for i in inputSTR_X:
        if i == "1" and inputSTR_Y[j] == "1" or i == "0" and inputSTR_Y[j] == "0":
            outputSTR = outputSTR + "0"
        else:
            outputSTR = outputSTR + "1"
        j += 1
    return outputSTR 

    
if __name__== "__main__":
    condition00X = "010111001010100001100011"
    condition00Y = "010000110001011100101001"

    condition01 = condNOT(condition00X)
    condition02 = condAND(condition00X, condition00Y)
    condition03 = condOR(condition00X, condition00Y)
    condition04 = conXOR(condition00X, condition00Y)
    print (condition01,"\n",condition02,"\n",condition03,"\n",condition04)
    
    print("Ans:")
    Ch4P4_3a = "10011001"
    Ch4P4_3b = "10011001"
    Ch4P4_3c = "11111111"
    Ch4P4_3d = "11111111"
    print("========")
    Ch4P4_4a = "01100110"
    Ch4P4_4b = "11111111"
    Ch4P4_4c = "00010001"
    Ch4P4_4d = "10111011"
    print("========")
    Ch4P4_13a = "0000010010100000 = 1184"
    Ch4P4_13b = "1111110010100010 = -862"
    Ch4P4_13c = "0000001101011110 = 862"
    Ch4P4_13d = "1111101101100000 = -1184"
    print("========")
    Ch4P4_15a = "overflow"
    Ch4P4_15b = "no overflow"
    Ch4P4_15c = "no overflow"
    Ch4P4_15d = "overflow"
    print("========")
    Ch4P4_16a = "0F51"
    Ch4P4_16b = "0F2A"
    Ch4P4_16c = "8012"
    Ch4P4_16d = "7F51"    
        
    