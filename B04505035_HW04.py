#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def shitAND(x,y):
    outputSTR=""
    h=len(x)
    k=0
    while k<h:
        if int(x[k]) ==int(y[k])  and int(y[k])== 1 :
          outputSTR=outputSTR+"1" #每次縮排空四格。這行少了兩格。
        else :
          outputSTR=outputSTR+"0" #每次縮排空四格。這行少了兩格。
        k=k+1
    return outputSTR
def bitchOR(x,y):
    outputSTR= ""
    for league,legend in zip(x,y):
        if league==0 and legend==0:
            outputSTR=outputSTR+"0"
        else:
            outputSTR=outputSTR+"1"
    return outputSTR
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
    x=input()
    y=input()
    #再加點輸入提示. e.g., x = input("請輸入一字串：")，使用者才知道你要做什麼。


    loser=shit(x,y)
    print(loser)



    print("Ans:") #這是在 if __name__ == "__main__": 的區塊下的，需要縮排。
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