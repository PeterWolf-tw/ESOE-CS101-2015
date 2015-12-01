#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def condNOT(inputSTR_X):
    outputSTR = ""
    for i in inputSTR_X:
        if i == "0":
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
    return outputSTR

def condAND(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for i,j in zip (inputSTR_X , inputSTR_Y):
        if i==j:
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
    return outputSTR
def condOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for i,j in zip (inputSTR_X , inputSTR_Y):
        if (i == "1" or j == "1"):
             outputSTR = outputSTR + "1" #每次縮排縮四個空格。這裡多了一個空格。
        else:
             outputSTR = outputSTR + "0"   #每次縮排縮四個空格。這裡多了一個空格。
    return outputSTR
def conXOR(inputSTR_X, inputSTR_Y):
    outputSTR=""
    for i,j in zip (inputSTR_X , inputSTR_Y):
        if i != j:
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
    return outputSTR

print("What logical connective do you want")
i = 1
while i == 1:
    a = input("Please enter the logical connective you want, but only enter 'and, or, not, xor'")
    if a == "and":
        b= input("Please enter the first array")
        c= input("Please enter the second array")
        d = condAND(b, c)
        print(d)
    elif a == "or":
        b= input("Please enter the first array")
        c= input("Please enter the second array")
        d = condOR(b, c)
        print(d)
    elif a == "xor":
        b= input("Please enter the first array")
        c= input("Please enter the second array")
        d = conXOR(b, c)
        print(d)
    elif a=="not" :
        b= input("Please enter the array")
        d = condNOT(b)
        print(d)
    else:
        print("ERROR")
def hex2bin(hexSTR):
    output= ""
    for i in hexSTR:
        if i =="0":
            output= output+"0000"
        elif i =="1":
            output= output+"0001"
        elif i =="2":
            output= output+"0010"
        elif i =="3":
            output= output+"0011"
        elif i =="4":
            output= output+"0100"
        elif i =="5":
            output= output+"0101"
        elif i =="6":
            output= output+"0110"
        elif i =="7":
            output= output+"0111"
        elif i =="8":
            output= output+"1000"
        elif i =="9":
            output= output+"1001"
        elif i =="A":
            output= output+"1010"
        elif i =="B":
            output= output+"1011"
        elif i =="C":
            output= output+"1100"
        elif i =="D":
            output= output+"1101"
        elif i =="E":
            output= output+"1110"
        elif i =="F":
            output= output+"1111"
        else:
            print("ERROR")
    return output

print("Ans:")
def ans(n):
    o=hex2bin(n)

    print("Ch4P4_3a = 10011001")
    print("Ch4P4_3b = 11111111")
    print("Ch4P4_3c = 10011001 ")
    print("Ch4P4_3d = 11111111")
    print("========")
    Ch4P4_4a = "01100110"
    Ch4P4_4b = "11111111"
    Ch4P4_4c = "00010001"
    Ch4P4_4d = "10111011"
    print("========")
    Ch4P4_13a = "65148" #1184
    Ch4P4_13b = "57662" #-862
    Ch4P4_13c = "-57662" #862
    Ch4P4_13d = "-65148" #-1184
    print("========")
    Ch4P4_15a = "overflow"
    Ch4P4_15b = "no" #-73
    Ch4P4_15c = "no" #73
    Ch4P4_15d = "overflow"
    print("========")
    Ch4P4_16a = "0F51"
    Ch4P4_16b = "overflow" #0F2A
    Ch4P4_16c = "overflow" #8012
    Ch4P4_16d = "overflow" #7F51
