#!/usr/bin/env python3
# -*- coding:utf-8 -*-

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
    for i in range(max(len(inputSTR_X), len(inputSTR_Y))):
        if inputSTR_X[i] == '1' and inputSTR_Y[i] == '1':
            outputSTR += '1'
        else :
            outputSTR += '0'
    return outputSTR

#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for i in range(max(len(inputSTR_X), len(inputSTR_Y))):
        if inputSTR_X[i] == '1' or inputSTR_Y[i] == '1':
            outputSTR += '1'
        else :
            outputSTR += '0'
    return outputSTR

#condition00 xor condition04
def condXOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for i in range(max(len(inputSTR_X), len(inputSTR_Y))):
        if inputSTR_X[i] != inputSTR_Y[i] :
            outputSTR += "1"
        else :
            outputSTR += "0"
    return outputSTR

#convert hex to bin
def hex2Bin(hexSTR):
    return bin(int(hexSTR, 16))[2:]

if __name__== "__main__":
    
    print("Please enter two binary numbers in same length:")
    condition00X = input()#"010111001010100001100011"
    condition00Y = input()#"010000110001011100101001"
    if len(condition00X) != len(condition00Y) :
        print("Invalid input.")
    else :
        print('\n'+condNOT(condition00X))
        print(condAND(condition00X, condition00Y))
        print(condOR(condition00X, condition00Y))
        print(condXOR(condition00X, condition00Y)+'\n')
    
    print("Ans:")
    Ch4P4_3a = "10011001"
    print(Ch4P4_3a)
    Ch4P4_3b = "10011001"
    print(Ch4P4_3b)
    Ch4P4_3c = "11111111"
    print(Ch4P4_3c)
    Ch4P4_3d = "11111111"
    print(Ch4P4_3d)
    print("========")
    Ch4P4_4a = "01100110"
    print(Ch4P4_4a)
    Ch4P4_4b = "11111111"
    print(Ch4P4_4b)
    Ch4P4_4c = "00010001"
    print(Ch4P4_4c)
    Ch4P4_4d = "10111011"
    print(Ch4P4_4d)
    print("========")
    Ch4P4_13a = "0000010010100000 = 1184"
    print(Ch4P4_13a)
    Ch4P4_13b = "1111110010100010 = -862"
    print(Ch4P4_13b)
    Ch4P4_13c = "0000001101011110 = 862"
    print(Ch4P4_13c)
    Ch4P4_13d = "1111101101100000 = -1184"
    print(Ch4P4_13d)
    print("========")
    Ch4P4_15a = "10001001(overflow) = -119"
    print(Ch4P4_15a)
    Ch4P4_15b = "10110111 = -73"
    print(Ch4P4_15b)
    Ch4P4_15c = "01001001 = 73"
    print(Ch4P4_15c)
    Ch4P4_15d = "01110111(overflow) = 119"
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
    