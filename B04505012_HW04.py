#!/usr/bin/env python 3
#-*- coding:utf-8 -*-

#condition00 not condition01 
def NOT(inputSTR_X): 
    outputSTR = "" 
    for i in inputSTR_X: 
        if i == "0": 
            outputSTR = outputSTR + "1" 
        else: 
            outputSTR = outputSTR + "0" 
    return outputSTR

def AND(X,Y): 
    outputSTR = "" 
    L1 = len(X)             
    L2 = len(Y)             
    if L1 == L2 :               
        for i in range(0,L1):        
            if str (X[i]) == str (Y[i]) ==  "1":     
                outputSTR = outputSTR + "1" 
            else: 
                outputSTR = outputSTR + "0"
    else :
        outputSTR="輸入字串錯誤"
    return outputSTR

def OR(X,Y): 
    outputSTR = "" 
    L1= len(X)             
    L2= len(Y)             
    if L1 == L2 :               
        for i in range(0,L1):       
            if str(X[i]) == "1" or str(Y[i]) == "1":     
                outputSTR = outputSTR + "1" 
            else: 
                outputSTR = outputSTR + "0" 
    else :
        outputSTR="輸入字串錯誤"
    return outputSTR

def XOR(X,Y): 
    outputSTR = "" 
    L1 = len(X)           
    L2 = len(Y)             
    if L1 == L2 :               
        for i in range(0,L1):        
            if str(X[i]) != str(Y[i]):     
                outputSTR = outputSTR + "1" 
            else: 
                outputSTR = outputSTR + "0" 
    else :
        outputSTR="輸入字串錯誤"
    return outputSTR

def hex2Bin(hexSTR): 
    ''' 
    16 進位表示式轉為 2 進位表示式 
    '''
    
    return bin(int(hexSTR, 16))[2:] 


if __name__ == "__main__":
    X = input("請輸入一個二進位數: ")
    Y = input("請輸入和上一個長度相同二進位數: ")

    condition01 = NOT(X)
    
    print(" NOT " + condition01)

    condition02 = AND(X,Y)
     
    print(" AND " + condition02)

    condition03 = OR(X,Y)
    
    print(" OR " + condition03)

    condition04 = XOR(X,Y)
    
    print(" XOR " + condition04)