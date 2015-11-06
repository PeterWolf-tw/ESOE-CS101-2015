#!/usr/bin/env python 3
#-*- coding:utf-8 -*-

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
    b = 0
    for a in inputSTR_X:
        if a == "1" and inputSTR_Y[b] == "1":
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
        b += 1
    return outputSTR

#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    b = 0
    for a in inputSTR_X:
        if a == "0" and inputSTR_Y[b] == "0":
            outputSTR = outputSTR + "0"
        else:
            outputSTR = outputSTR + "1"
        b += 1
    return outputSTR

#condition00 xor condition04
def condXOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    b = 0
    for a in inputSTR_X:
        if a == inputSTR_Y[b]:
            outputSTR = outputSTR + "0"
        else:
            outputSTR = outputSTR + "1"
        b += 1
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
    condition02 = condAND(condition00X, condition00Y)
    print(condition02)
    condition03 = condOR (condition00X, condition00Y)
    print(condition03)
    condition04 = condXOR(condition00X, condition00Y)
    print(condition04)
    print("========")
    
    #可利用 hex2Bin() 函式計算十六進位表示式 "99" 的二進位表式：(範例如下)
    a = hex2Bin("99")
    print("99 hexadecimal to binary is {0}!!". format(a))
    b = hex2Bin("00")
    print("00 hexadecimal to binary is {0}!!". format(b))
    c = hex2Bin("FF")
    print("FF hexadecimal to binary is {0}!!". format(c))
    d = hex2Bin("33")
    print("33 hexadecimal to binary is {0}!!". format(d))
    print("========")
    
    
    
    
    
    print("Ans:")
    Ch4P4_3a = "1001 1001"
    print("Ch4P4_3a = {0}". format(Ch4P4_3a))
    Ch4P4_3b = "1001 1001"
    print("Ch4P4_3b = {0}". format(Ch4P4_3b))
    Ch4P4_3c = "1111 1111"
    print("Ch4P4_3c = {0}". format(Ch4P4_3c))
    Ch4P4_3d = "1111 1111"
    print("Ch4P4_3d = {0}". format(Ch4P4_3d))
    print("========")
    Ch4P4_4a = "0110 0110"
    print("Ch4P4_4a = {0}". format(Ch4P4_4a))
    Ch4P4_4b = "1111 1111"
    print("Ch4P4_4b = {0}". format(Ch4P4_4b))
    Ch4P4_4c = "0001 0001"
    print("Ch4P4_4c = {0}". format(Ch4P4_4c))
    Ch4P4_4d = "1011 1011"
    print("Ch4P4_4d = {0}". format(Ch4P4_4d))
    print("========")
    Ch4P4_13a = "0000 0100 10100 000"
    a2dec = 1184
    print("Ch4P4_13a = {0}, {1} after converted todecimal.". format(Ch4P4_13a, a2dec))
    Ch4P4_13b = "1111 1100 1010 0010"
    b2dec = -862
    print("Ch4P4_13b = {0}, {1} after converted todecimal.". format(Ch4P4_13b, b2dec))
    Ch4P4_13c = "0000 0011 0101 1110"
    c2dec = 862
    print("Ch4P4_13c = {0}, {1} after converted todecimal.". format(Ch4P4_13c, c2dec))
    Ch4P4_13d = "1111 1011 0110 0000"
    d2dec = -1184
    print("Ch4P4_13d = {0}, {1} after converted todecimal.". format(Ch4P4_13d, d2dec))
    print("========")
    Ch4P4_15a = "positive overflow"
    print("Ch4P4_15a = {0}". format(Ch4P4_15a))
    Ch4P4_15b = "won't overflow"
    print("Ch4P4_15b = {0}". format(Ch4P4_15b))
    Ch4P4_15c = "won't overflow"
    print("Ch4P4_15c = {0}". format(Ch4P4_15c))
    Ch4P4_15d = "negative overflow"
    print("Ch4P4_15d = {0}". format(Ch4P4_15d))
    print("========")
    Ch4P4_16a = "0F51"
    print("Ch4P4_16a = {0}". format(Ch4P4_16a))
    Ch4P4_16b = "0F2A"
    print("Ch4P4_16b = {0}". format(Ch4P4_16b))
    Ch4P4_16c = "8012"
    print("Ch4P4_16c = {0}". format(Ch4P4_16c))
    Ch4P4_16d = "7F51(overflow)" 
    print("Ch4P4_16d = {0}". format(Ch4P4_16d))