#!/usr/bin/env python 3
#-*- coding:utf-8 -*-

#condition00 not condition01 
def condNOT(inputSTR_X): 
    outputSTR = "" 
    for i in inputSTR_X: 
        if i == "0": 
            outputSTR = outputSTR + "1" 
        else: 
            outputSTR = outputSTR + "0" 
    return outputSTR

def condAND(inputSTR_X,inputSTR_Y): 
    outputSTR = "" 
    lengthX = len(inputSTR_X)             # inputSTR_X字串長度
    lengthY = len(inputSTR_Y)             # inputSTR_Y字串長度
    if lengthX == lengthY :               # 兩個字串長度相等才轉換
        for i in range(0,lengthX):        #i 從 0 到 length-1
            if str(inputSTR_X[i]) == str(inputSTR_Y[i]) == "1":     
                outputSTR = outputSTR + "1" 
            else: 
                outputSTR = outputSTR + "0"
    else :
        outputSTR="字串錯誤"
    return outputSTR

def condOR(inputSTR_X,inputSTR_Y): 
    outputSTR = "" 
    lengthX = len(inputSTR_X)             # inputSTR_X字串長度
    lengthY = len(inputSTR_Y)             # inputSTR_Y字串長度
    if lengthX == lengthY :               # 兩個字串長度相等才轉換
        for i in range(0,lengthX):        #i 從 0 到 length-1
            if str(inputSTR_X[i]) == "1" or str(inputSTR_Y[i]) == "1":     
                outputSTR = outputSTR + "1" 
            else: 
                outputSTR = outputSTR + "0" 
    else :
        outputSTR="字串錯誤"
    return outputSTR

def condXOR(inputSTR_X,inputSTR_Y): 
    outputSTR = "" 
    lengthX = len(inputSTR_X)             # inputSTR_X字串長度
    lengthY = len(inputSTR_Y)             # inputSTR_Y字串長度
    if lengthX == lengthY :               # 兩個字串長度相等才轉換
        for i in range(0,lengthX):        #i 從 0 到 length-1
            if str(inputSTR_X[i]) != str(inputSTR_Y[i]):     
                outputSTR = outputSTR + "1" 
            else: 
                outputSTR = outputSTR + "0" 
    else :
        outputSTR="字串錯誤"
    return outputSTR

def hex2Bin(hexSTR): 
    ''' 
    16 進位表示式轉為 2 進位表示式 
    '''
    
    return bin(int(hexSTR, 16))[2:] 


if __name__ == "__main__":
    condition00X = "010111001010100001100011"
    condition00Y = "010000110001011100101001"

    condition01 = condNOT(condition00X)
    
    print('con01='+condition01)

    condition02 = condAND(condition00X,condition00Y)
    
    
    print('con02='+condition02)

    condition03 = condOR(condition00X,condition00Y)
    
    
    print('con03='+condition03)

    condition04 = condXOR(condition00X,condition00Y)
    
    
    print('con04='+condition04)
    
    
    print("Ch4P4_3a =1001 1001")
    print("Ch4P4_3b =1001 1001")
    print("Ch4P4_3c =1111 1111")
    print("Ch4P4_3d =1111 1111")
    print("Ch4P4_4a =0110 0110")
    print("Ch4P4_4b =1111 1111")
    print("Ch4P4_4c =0001 0001")
    print("Ch4P4_4d =1011 1011")
    print("Ch4P4_13a =0000 0100 1010 0000")
    print("Ch4P4_13b =1111 1100 1010 0010")
    print("Ch4P4_13c =0000 0011 0101 1110")
    print("Ch4P4_13d =1111 1011 0110 0000")
    print("Ch4P4_15a =overflow")
    print("Ch4P4_15b =won\'t overflow")
    print("Ch4P4_15c =overflow")
    print("Ch4P4_15d =won\'t overflow")
    print("Ch4P4_16a =0F51")
    print("Ch4P4_16b =0F2A")
    print("Ch4P4_16c =8012")
    print("Ch4P4_16d =7F51")
