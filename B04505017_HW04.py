#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def condNOT(strx):
    out = ""
    for i in strx:
        if i == "0":
            out = out + "1"
        else:
            out = out + "0"
    return out
def condAND(strx,stry):
    out = ""
    for i,j in zip(strx,stry):
        if (i == "1" and j =="1") :
            out = out + "1"
        else:
            out = out + "0"
    return out
def condOR(strx,stry):
    out = ""
    for i,j in zip(strx,stry):
        if (i == "0" and j =="0") :
            out = out + "0"
        else:
            out = out + "1"
    return out
def condXOR(strx,stry):
    out = ""
    for i,j in zip(strx,stry):
        if i == j:
            out = out + "0"
        else:
            out = out + "1"
    return out

if __name__== "__main__":

    print ("What logical connective do you want to do?")
    i = 1
    while i == 1:
        print(" ")
        a = input("Please use capital letters. And ONLY in AND,OR,XOR,NOT.")
        print(" ")
        if a == "OR":
            a = input("Input the  first array: ")
            print(" ")
            b = input("Input the second array: ")
            print(" ")
            c = condOR(a,b)
            print(c)
        elif a == "AND":
            a = input("Input the  first array: ")
            print(" ")
            b = input("Input the second array: ")
            print(" ")
            c = condAND(a,b)
            print(c)
        elif a == "XOR":
            a = input("Input the  first array: ")
            print(" ")
            b = input("Input the second array: ")
            print(" ")
            c = condXOR(a,b)
            print(c)
        elif a == "NOT":
            a = input("Input the   only array: ")
            print(" ")
            c = condNOT(a)
            print(c)
        else:
            print("What are you doing? Stupid")
            print(" ")
            print("I will give you another chance. But DON'T do it again. NOODLE")
    '''

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
        Ch4P4_13a = "1184"
        Ch4P4_13b = "-862"
        Ch4P4_13c = "862"
        Ch4P4_13d = "-1184"
    print("========")
        Ch4P4_15a = "overflow"
        Ch4P4_15b = "no"
        Ch4P4_15c = "no"
        Ch4P4_15d = "overflow"
    print("========")
        Ch4P4_16a = "0F51"
        Ch4P4_16b = "overflow?,0F2A"
        Ch4P4_16c = "overflow!!,-7FEE"
        Ch4P4_16d = "overflow...,7F51"

    '''