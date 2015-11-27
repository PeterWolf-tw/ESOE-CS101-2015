#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#░░░░░░░░░░░░░░░░░░░░░░░░░░
#░░░░░░░░░░░░░▄███▄▄▄░░░░░░
#░░░░░░░░░▄▄▄██▀▀▀▀███▄░░░░
#░░░░░░░▄▀▀░░░░░░░░░░░▀█░░░
#░░░░▄▄▀░░░░░░░░░░░░░░░▀█░░                   ░     ░         ░░░░░         ░░░░░░
#░░░█░░░░░▀▄░░▄▀░░░░░░░░█░░                    ░   ░          ░             ░
#░░░▐██▄░░▀▄▀▀▄▀░░▄██▀░▐▌░░                      ░            ░░░░          ░░░░░
#░░░█▀█░▀░░░▀▀░░░▀░█▀░░▐▌░░                      ░            ░             ░
#░░░█░░▀▐░░░░░░░░▌▀░░░░░█░░                      ░            ░░░░░         ░░░░░░
#░░░█░░░░░░░░░░░░░░░░░░░█░░
#░░░░█░░▀▄░░░░▄▀░░░░░░░░█░░
#░░░░█░░░░░░░░░░░▄▄░░░░█░░░
#░░░░░█▀██▀▀▀▀██▀░░░░░░█░░░
#░░░░░█░░▀████▀░░░░░░░█░░░░
#░░░░░░█░░░░░░░░░░░░▄█░░░░░
#░░░░░░░██░░░░░█▄▄▀▀░█░░░░░
#░░░░░░░░▀▀█▀▀▀▀░░░░░░█░░░░
#░░░░░░░░░█░░░░░░░░░░░░█░░░ #Cute
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
    x=str(inputSTR_X)
    y=str(inputSTR_Y)
    L=len(x)
    for i in range(0,L):
        if x[i]=="1" and y[i]=="1" :
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
    return outputSTR

def condOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    x=str(inputSTR_X)
    y=str(inputSTR_Y)
    L=len(x)
    for i in range(0,L):
        if x[i]=="1" or y[i]=="1" :
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
    return outputSTR

def condXOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    x=str(inputSTR_X)
    y=str(inputSTR_Y)
    L=len(x)
    for i in range(0,L):
        if x[i]=="1" or y[i]=="1" :
            if x[i]=="1" and y[i]=="1":
                outputSTR = outputSTR + "0"
            else:
                outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
    return outputSTR

if __name__== "__main__":
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



##############################
#4-3
#a=1001 1001
#b=0000 0000 #10011001
#c=1001 1001
#d=1111 1111
############################
#4-4
#a=0110 0110
#b=1111 1111
#c=0001 0001
#d=1011 1011
##############################
#4-13
#a=0000 0100 1010 0000
#b=1111 1100 1010 0010
#c=0000 0011 0101 1110
#d=1111 1011 0110 0000
#############################
#4-15
#a=overfloat #It's "overflow"
#b=ok
#c=ok
#d=overfloat #It's "overflow"
#############################
#4-16
#a=0F51
#b=0F2A
#c=8012
#d=overfloat #It's "overflow"