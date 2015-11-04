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
    resultAND = ""
    if len(inputSTR_X) != len(inputSTR_Y) :
        if len(inputSTR_X) > len(inputSTR_Y) :
            inputSTR_Y = (len(inputSTR_X) - len(inputSTR_Y))* "0" + inputSTR_Y
        else :
            inputSTR_X = (len(inputSTR_Y) - len(inputSTR_X))* "0" + inputSTR_X 
    L = len(inputSTR_X)
    for i in range (0,L):
        if inputSTR_X[i] == inputSTR_Y[i] == "1" :
            k = "1"
        else : 
            k = "0"
        resultAND = resultAND + k 
    return resultAND

#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    resultOR = ""
    if len(inputSTR_X) != len(inputSTR_Y) :
        if len(inputSTR_X) > len(inputSTR_Y) :
            inputSTR_Y = (len(inputSTR_X) - len(inputSTR_Y))* "0" + inputSTR_Y
        else:
            inputSTR_X = (len(inputSTR_Y) - len(inputSTR_X))* "0" + inputSTR_X 
    L = len(inputSTR_X)
    for i in range (0,L):
        if inputSTR_X[i] == inputSTR_Y[i] == "0" :
            k = "0"
        else : 
            k = "1"
        resultOR = resultOR + k 
    return resultOR
#condition00 xor condition04
def conXOR(inputSTR_X, inputSTR_Y):
    resultXOR = ""
    if len(inputSTR_X) != len(inputSTR_Y) :
        if len(inputSTR_X) > len(inputSTR_Y) :
            inputSTR_Y = (len(inputSTR_X) - len(inputSTR_Y))* "0" + inputSTR_Y
        else :
            inputSTR_X = (len(inputSTR_Y) - len(inputSTR_X))* "0" + inputSTR_X 
    L = len(inputSTR_X)
    for i in range (0,L):
        if inputSTR_X[i] == inputSTR_Y[i] :
            k = "0"
        else : 
            k = "1"
        resultOR = resultOR + k 
    return resultXOR


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
    
    X = input("輸入X值\n")
    Y = input("輸入Y值\n")
    print ("X AND Y = ")
    print(condAND(X, Y))

    #可利用 hex2Bin() 函式計算十六進位表示式 "99" 的二進位表式：(範例如下)
    b = hex2Bin("99")
    print(b)


    print("Ans:")
    Ch4P4_3a = "10011001"
    Ch4P4_3b = "11111111"
    Ch4P4_3c = "10011001"
    Ch4P4_3d = "11111111"
    print("========")
    Ch4P4_4a = "01100110"
    Ch4P4_4b = "11111111"
    Ch4P4_4c = "10001"
    Ch4P4_4d = "10111011"
    print("========")
    Ch4P4_13a = "0000010010100000 = 1184"
    Ch4P4_13b = "1111110010100010 = -862"
    Ch4P4_13c = "0000001101011110 = 862"
    Ch4P4_13d = "1111101101100000 = -1184"
    print("========")
    Ch4P4_15a = "10001001 = -119 (overflow)"
    Ch4P4_15b = "10110111 = -73"
    Ch4P4_15c = "01001001 = 73"
    Ch4P4_15d = "01110111 = 119 (overflow)"
    print("========")
    Ch4P4_16a = "0F51"
    Ch4P4_16b = "0F2A"
    Ch4P4_16c = "8012"
    Ch4P4_16d = "7F51"    