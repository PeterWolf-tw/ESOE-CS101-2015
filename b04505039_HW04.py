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
    for i , k in zip(inputSTR_X,inputSTR_Y) :
        if i == "1" and k == "1" :
            outputSTR = outputSTR + "1"
        else  :
            outputSTR = outputSTR + "0"
    return outputSTR


#if __name__== "__main__":
    #condition00X = "010111001010100001100011"
    #condition00Y = "010000110001011100101001"

    #condition02 = condAND(condition00X,condition00Y)
    #print(condition02)



#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for i,k in zip(inputSTR_X, inputSTR_Y):
        if i == "0" and k == "0" :
            outputSTR = outputSTR + "0"
        else :
            outputSTR = outputSTR + "1"
    return outputSTR


#if __name__== "__main__":
    #condition00X = "010111001010100001100011"
    #condition00Y = "010000110001011100101001"

    #condition03 = condOR(condition00X,condition00Y)
    #print(condition03)

#condition00 xor condition04
def condXOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for i,k in zip(inputSTR_X, inputSTR_Y):
        if i == k: #沒加冒號，會造成句法錯誤 (SyntaxError)
            outputSTR = outputSTR + "0"
        else :
            outputSTR = outputSTR + "1"
#if __name__== "__main__":
     #condition00X = "010111001010100001100011"
     #condition00Y = "010000110001011100101001"

     #condition04 = condXOR(condition00X,condition00Y)
     #print(condition04)






def hex2Bin(hexSTR):
    '''
    16 進位表示式轉為 2 進位表示式
    '''
    return bin(int(hexSTR, 16))[2:]


if __name__== "__main__": # if __name__ == "__main__": 這行是程式的進入點。一個程式只有「一個」進入點，而不是每個 function 都有自己的進入點。    condition00X = "010111001010100001100011"
    condition00X = "010111001010100001100011"
    condition00Y = "010000110001011100101001"

    condition01 = condNOT(condition00X)
    print(condition01)
    condition02 = condAND(condition00X,condition00Y)
    print(condition02)
    condition03 = condOR(condition00X,condition00Y)
    print(condition03)
    condition04 = condXOR(condition00X,condition00Y)
    print(condition04)



    #可利用 hex2Bin() 函式計算十六進位表示式 "99" 的二進位表式：(範例如下)
    b = hex2Bin("99") #hex2Bin() 轉的是字串，不是數字。
    print(b)


    print("Ans:") #縮排一次四個空格。不要任意更動。
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