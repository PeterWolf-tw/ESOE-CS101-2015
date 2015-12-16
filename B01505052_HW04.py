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
    l=len(inputSTR_X)
    #algorithm
    for i in range(0,l):
        output=int(inputSTR_X[i])*int(inputSTR_Y[i])
        if output==0:
            outputSTR = outputSTR + "0"
        else:
            outputSTR = outputSTR + "1"

    print(outputSTR) #Python3 的 print() 要加括號哦！

#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):

    outputSTR = ""
    l=len(inputSTR_X)
    #algorithm
    for i in range(0,l):
        if inputSTR_X[i]=="1":
            outputSTR = outputSTR + "1"
        elif inputSTR_Y[i]=="1":
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"

    print(outputSTR) #Python3 的 print() 要加括號哦！

#condition00 xor condition04
def condXOR(inputSTR_X, inputSTR_Y):

    outputSTR = ""
    l=len(inputSTR_X)
    #algorithm
    for i in range(0,l):
        if inputSTR_X[i]=="1" and inputSTR_Y[i]=="1":
            outputSTR = outputSTR + "0"
        elif inputSTR_X[i]=="0" and inputSTR_Y[i]=="0":
            outputSTR = outputSTR + "0"
        else:
            outputSTR = outputSTR + "1"

    print(outputSTR) #Python3 的 print() 要加括號哦！


def hex2Bin(hexSTR):
    '''
    16 進位表示式轉為 2 進位表示式
    '''
    return str(bin(int(hexSTR, 16)))[2:]


if __name__== "__main__":
    condition00X = "010111001010100001100011"
    condition00Y = "010000110001011100101001"
    condition01 = condNOT(condition00X)
    print(condition01)
    condAND(condition00X,condition00Y)
    condOR(condition00X,condition00Y)
    condXOR(condition00X,condition00Y)


    #可利用 hex2Bin() 函式計算十六進位表示式 "99" 的二進位表式：(範例如下)
    b = hex2Bin("99")
    print(b)
    c = hex2Bin("FF")
    print(c)
    d = hex2Bin("00")
    print(d)
    e = hex2Bin("33")
    print(e)

    #P4-3
    print("4-3(a). 10011001")
    print("4-3(b). 11111111")
    print("4-3(c). 10011001")
    print("4-3(d). 11111111")
    print(" ")
    #P4-4
    print("4-4(a). 01100110")
    print("4-4(b). 11111111")
    print("4-4(c). 00010001")
    print("4-4(d). 10111011")
    print(" ")
    #P4-13
    print("4-13(a). 1184")
    print("4-13(b). -862")
    print("4-13(c). 862")
    print("4-13(d). -1184")
    print(" ")
    #P4-15
    print("4-15(a). overflow")
    print("4-15(b). 73") #-73
    print("4-15(c). 73")
    print("4-15(d). overflow")
    print(" ")
    #P4-16
    print("4-16(a). 0F51")
    print("4-16(b). 0F2A")
    print("4-16(c). 8012")
    print("4-16(d). 7F51")