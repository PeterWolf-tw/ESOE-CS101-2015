Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 

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
    for a, b in zip(inputSTR_X, inputSTR_Y):
        if a == "0" or b == "0":
            outputSTR = outputSTR + "0"
        else:
            outputSTR = outputSTR + "1"
    return outputSTR

#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for a, b in zip(inputSTR_X, inputSTR_Y):
        if a == "1" or b == "1":
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
    return outputSTR

#condition00 xor condition04
def condXOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for a, b in zip(inputSTR_X, inputSTR_Y):
        if a == b:
            outputSTR = outputSTR + "0"
        else:
            outputSTR = outputSTR + "1"
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
    print("condition01 = ",condition01)
    condition02 = condAND(condition00X,condition00Y)
    print("condition02 = ",condition02)
    condition03 = condOR(condition00X,condition00Y)
    print("condition03 = ",condition03)
    condition04 = condXOR(condition00X,condition00Y)
    print("condition04 = ",condition04)

    #可利用 hex2Bin() 函式計算十六進位表示式 "99" 的二進位表式：(範例如下)
    b = hex2Bin("99")
    print(b)


    print("Ans:")
    print("")
    Ch4P4_3a = condOR(hex2Bin("99"), hex2Bin("99"))
    print("4-3a:")
    print(Ch4P4_3a)
    print("")
    Ch4P4_3b = condOR(hex2Bin("99"), hex2Bin("FF"))
    print("4-3b:")
    print(Ch4P4_3b)
    print("")
    Ch4P4_3c = condOR(hex2Bin("99"), hex2Bin("00 "))
    print("4-3c:")
    print(Ch4P4_3c)
    print("")
    Ch4P4_3d = condOR(hex2Bin("FF"), hex2Bin("FF"))
    print("4-3d:")
    print(Ch4P4_3d)
    print("")
    print("Ans:")
    print("")
    Ch4P4_4a = condNOT(condOR(hex2Bin("99"), hex2Bin("99")))
    print("4-4a:")
    print(Ch4P4_4a)
    print("")
    Ch4P4_4b = condOR(hex2Bin("99"),condNOT("00"))
    print("4-4b:")
    print(Ch4P4_4b)
    print("")
    Ch4P4_4c = condOR(condAND(hex2Bin("99"),hex2Bin("33")),condAND(hex2Bin("00"),hex2Bin("FF")))
    print("4-4c:")
    print(Ch4P4_4c)
    print("")
    Ch4P4_4d = condAND(condOR(hex2Bin("99"),hex2Bin("33")),condOR(hex2Bin("00"),hex2Bin("FF")))
    print("4-4d:")
    print(Ch4P4_4d)
    print("")
    print("")
    print("4_13a = 0000 0100 1010 0000 ( 1184)" )
    print("4_13b = 1111 1100 1010 0010 (-862 )" )
    print("4_13c = 0000 0011 0101 1110 ( 862 )"  )
    print("4_13d = 1111 1011 0110 0000 (-1184)")
    print("")
    print("")
    print("4_15a = 1000 1001 (-119[overflow])")
    print("4_15b = 1011 0111 (-73[non-overflow])")
    print("4_15c = 0100 1001 ( 73[non-overflow])")
    print("4_15d = 0111 0111 ( 119[overflow])")
    print("")
    print("")
    print("4_16a = 0000 1111 0101 0001  (0F51)")
    print("4_16b = 0000 1111 0010 1010  (0F2A)")
    print("4_16c = 1000 0000 0001 0010  (8012)")
    print("4_16d = 0111 1111 0101 0001  (7F51[overflow])") 
