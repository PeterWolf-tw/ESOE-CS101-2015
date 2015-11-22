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
inputSTR_X = input("number:")
print(condNOT(inputSTR_X))

#condition00 and condition02
def condAND(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for i in inputSTR_X:
        for j in inputSTR_Y:
            if i and j == "1":
                outputSTR = outputSTR + "1"
            else:
                outputSTR = outputSTR + "0"
    return outputSTR
inputSTR_X = input("number1:")
inputSTR_Y = input("number2:")
print(condAND(inputSTR_X, inputSTR_Y))

#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for i in inputSTR_X:
        for j in inputSTR_Y:
            if i and j == "0":
                outputSTR = outputSTR + "0"
            else:
                outputSTR = outputSTR + "1"
    return outputSTR
inputSTR_X = input("number1:")
inputSTR_Y = input("number2:")
print(condAND(inputSTR_X, inputSTR_Y))
      
#condition00 xor condition04
def condXOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for i in inputSTR_X:
        for j in inputSTR_Y:
            if i and j == "0":
                outputSTR = outputSTR + "0"
            elif i and j == "1":
                outputSTR = outputSTR + "0"
            else:
                outputSTR = outputSTR + "1"
    return outputSTR
inputSTR_X = input("number1:")
inputSTR_Y = input("number2:")
print(condAND(inputSTR_X, inputSTR_Y))

if __name__ == "__main__":
    condition00X = "010111001010100001100011"
    condition00Y = "010000110001011100101001"    
    
    condition01 = condNOT(condition00X)
    print(condition01)
    condition02 = condAND(condition00X, condition00Y)
    print(condition02)
    condition03 = condOR(condition00X, condition00Y)
    print(condition03)
    condition04 = condXOR(condition00X, condition00Y)
    print(condition04)
    
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
        Ch4P4_13a = "0000010010100000=1184"
        Ch4P4_13b = "1111110010100010=-862"
        Ch4P4_13c = "0000001101011110=862"
        Ch4P4_13d = "1111101101100000=-1184"
    print("========")
        Ch4P4_15a = "-119  (overflow)"
        Ch4P4_15b = "-73  (no overflow)"
        Ch4P4_15c = "73  (no overflow)"
        Ch4P4_15d = "119  (overflow)"
    print("========")
        Ch4P4_16a = "0F51"
        Ch4P4_16b = "0F2A"
        Ch4P4_16c = "8012"
        Ch4P4_16d = "7F51  (overflow)"    
