#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#請參考以下 condNOT() 的例子，設計四個 func() 依以下條件，能算出 condition02 ~ 04 的值

#condition00 not condition01
def condNOT(inputSTR_X):
    outputSTR = ""
    for i in inputSTR_X:
        if i == "0":
            outputSTR += "1"
        else:
            outputSTR += "0"
    return outputSTR

#condition00 and condition02
def condAND(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for i,j in zip(inputSTR_X,inputSTR_Y):
        if i == "1" and j == "1":
            outputSTR += "1"
        else:
            outputSTR += "0"
    return outputSTR

#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for i,j in zip(inputSTR_X,inputSTR_Y):        
        if i == "0" and j == "0":
            outputSTR += "0"
        else:
            outputSTR += "1"
    return outputSTR

#condition00 xor condition04
def condXOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for i,j in zip(inputSTR_X,inputSTR_Y):        
        if i == "1" and j == "1":
            outputSTR += "0"
        elif i == "0" and j == "0":
            outputSTR += "0"
        else:
            outputSTR += "1"
    return outputSTR


def hex2Bin(hexSTR):
    '''
    16 進位表示式轉為 2 進位表示式
    '''
    return bin(int(hexSTR, 16))[2:]

a = int(input ("Choose one operation in NUMBER (1.Not/2.And/3.Or/4.Xor)\n"))

if a==1:
    condition00 = str(input("Input bit pattern: "))
    print(condNOT(condition00))

elif a==2 or 3 or 4 :
    conditionX = str(input("Input first bit pattern: "))
    conditionY = str(input("Input second bit pattern: "))
    if a==2:
        print(condAND(conditionX, conditionY))
    elif a==3:
        print(condOR(conditionX, conditionY))
    elif a==4:
        print(condXOR(conditionX, conditionY))
else:
    print ("Failed Input")


Ch4P4_3a = "10011001"
Ch4P4_3b = "11111111"
Ch4P4_3c = "10011001"
Ch4P4_3d = "11111111"
       
Ch4P4_4a = "01100110"
Ch4P4_4b = "11111111"
Ch4P4_4c = "10001"
Ch4P4_4d = "10111011"

Ch4P4_13a = "0000010010100000 = 1184"
Ch4P4_13b = "1111110010100010 = -862"
Ch4P4_13c = "0000001101011110 = 862"
Ch4P4_13d = "1111101101100000 = -1184"

Ch4P4_15a = "10001001 = -119 (overflow)"
Ch4P4_15b = "10110111 = -73"
Ch4P4_15c = "01001001 = 73"
Ch4P4_15d = "01110111 = 119 (overflow)"

Ch4P4_16a = "0F51"
Ch4P4_16b = "0F2A"
Ch4P4_16c = "8012"
Ch4P4_16d = "7F51"   