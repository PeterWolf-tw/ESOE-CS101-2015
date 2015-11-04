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
    for i, j in zip(inputSTR_X, inputSTR_Y):
        if i == j == "1":
            outputSTR += "1"
        else:
            outputSTR += "0"
            
    return outputSTR


#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for i, j in zip(inputSTR_X, inputSTR_Y):
        if i == j == "0":
            outputSTR += "0"
        else:
            outputSTR += "1"

    return outputSTR    


#condition00 xor condition04
def condXOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for i, j in zip(inputSTR_X, inputSTR_Y):
        if i == j:
            outputSTR += "0"
        else:
            outputSTR += "1"    
            
    return outputSTR


def hex2Bin(hexSTR):
    '''
    16 進位表示式轉為 2 進位表示式
    '''
    return bin(int(hexSTR, 16))[2:]


if __name__== "__main__":
    
    #可利用 hex2Bin() 函式計算十六進位表示式 "99" 的二進位表式：(範例如下)
    a = int(hex2Bin("8011"),2)
    b = int(hex2Bin("0001"),2)
    print(a)
    print(b)
    print(a+b)
    print(hex(a+b))
        
    condition00X = "10111011"
    condition00Y = "11111111"
    

    condition01 = condNOT(condition00X)
    print("NOT: " + condition01)
    condition01 = condAND(condition00X, condition00Y)
    print("AND: " + condition01)
    condition01 = condOR(condition00X, condition00Y)
    print("OR: " + condition01)
    condition01 = condXOR(condition00X, condition00Y)
    print("XOR: " + condition01)
    




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
    Ch4P4_15a = "-119(overflow) = 10001001"
    Ch4P4_15b = "-73 = 10110111"
    Ch4P4_15c = "73 = 01001001"
    Ch4P4_15d = "119(overflow) = 01110111"
    print("========")
    Ch4P4_16a = "0F51"
    Ch4P4_16b = "0F2A"
    Ch4P4_16c = "8012"
    Ch4P4_16d = "7F51"