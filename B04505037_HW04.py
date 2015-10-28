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


def hex2Bin(hexSTR):
    '''
    16 進位表示式轉為 2 進位表示式
    '''
    return bin(int(hexSTR, 16))[2:]



inputSTR_X = input("Please insert something: ")
inputSTR_Y = input("Insert again: ")
String = condOR(inputSTR_X, inputSTR_Y)
print(String)





#Ch4P4_3a = "10011001"
#Ch4P4_3b = "00000000"
#Ch4P4_3c = "10011001"
#Ch4P4_3d = "11111111"
print("========")
#Ch4P4_4a = "01100110"
#Ch4P4_4b = "11111111"
#Ch4P4_4c = "00010001"
#Ch4P4_4d = "10111011"
print("========")
#Ch4P4_13a = "0000010010100000 = 1184"
#Ch4P4_13b = "1111110010100010 = -862"
#Ch4P4_13c = "0000001101011110 = 862"
#Ch4P4_13d = "1111101101100000 = -1184"
print("========")
#Ch4P4_15a = "10001001 = -119"
#Ch4P4_15b = "10110111 = -73"
#Ch4P4_15c = "01001001 = 73"
#Ch4P4_15d = "01110111 = 119"
print("========")
#Ch4P4_16a = "0F51"
#Ch4P4_16b = "0F2A"
#Ch4P4_16c = "8012"
#Ch4P4_16d = "7F51"    