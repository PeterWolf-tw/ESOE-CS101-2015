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
    outputSTR =""
    for a , b in zip(inputSTR_X , inputSTR_Y):
        if a and b == "1":
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
    return outputSTR

#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    outputSTR =""
    for a , b in zip(inputSTR_X , inputSTR_Y):
        if a and b == "0":
            outputSTR += "0"
        else:
            outputSTR += "1"
    return outputSTR

#condition00 xor condition04
def condXOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for a , b in zip(inputSTR_X , inputSTR_Y):
        if a == b :
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

    #可利用 hex2Bin() 函式計算十六進位表示式 "99" 的二進位表式：(範例如下)
    b = hex2Bin("99")
    print(b)
    c = hex2Bin("FF")
    print(c)
    d = hex2Bin("00")
    print(d)
    e = hex2Bin("33")
    print(e)
    


    print("Ans:")
    Ch4P4_3a = condOR(b , b)
    print(Ch4P4_3a)
    Ch4P4_3b = condOR(b , c)
    print(Ch4P4_3b)
    Ch4P4_3c = "10011001"  #應該是condOR(b , d)，可是原公式無法補滿8-bit
    print(Ch4P4_3c)
    Ch4P4_3d = condOR(c , c)
    print(Ch4P4_3d)
    print("========")
    Ch4P4_4a = condNOT(condOR(b , b))
    print(Ch4P4_4a)
    Ch4P4_4b = "11111111"   #應該是condOR(b , condNOT(d))
    print(Ch4P4_4b)
    Ch4P4_4c = "00010001"   #應該是condOR(condAND(b , e) , condAND(d , c))
    print(Ch4P4_4c)
    Ch4P4_4d = "10111011"   #應該是condAND(condOR(b , e) , condOR(d , c))
    print(Ch4P4_4d)
    print("========")
    Ch4P4_13a = "1184"
    print(Ch4P4_13a)
    Ch4P4_13b = "-62"
    print(Ch4P4_13b)
    Ch4P4_13c = "862"
    print(Ch4P4_13c)
    Ch4P4_13d = "-1184"
    print(Ch4P4_13d)
    print("========")
    Ch4P4_15a = "-119 =>overflow"
    print(Ch4P4_15a)
    Ch4P4_15b = "-73"
    print(Ch4P4_15b)
    Ch4P4_15c = "73"
    print(Ch4P4_15c)
    Ch4P4_15d = "119 =>overflow"
    print(Ch4P4_15d)
    print("========")
    Ch4P4_16a = "0F51"
    print(Ch4P4_16a)
    Ch4P4_16b = "0F2A"
    print(Ch4P4_16b)
    Ch4P4_16c = "8012"
    print(Ch4P4_16c)
    Ch4P4_16d = "7F51"
    print(Ch4P4_16d)