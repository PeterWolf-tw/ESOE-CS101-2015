#!/usr/bin/python3
# -*- coding: utf-8 -*-

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
    for (i,j) in zip(inputSTR_X,inputSTR_Y):        
        if i == "1" and j == "1":
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
    return outputSTR

#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for (i,j) in zip(inputSTR_X,inputSTR_Y):        
        if i == "0" and j == "0":
            outputSTR = outputSTR + "0"
        else:
            outputSTR = outputSTR + "1"
    return outputSTR
    
#condition00 xor condition04
def condXOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for (i,j) in zip(inputSTR_X,inputSTR_Y):        
        if i == "0" and j == "0":
            outputSTR = outputSTR + "0"
        elif i == "1" and j == "1":
            outputSTR = outputSTR + "0"
        else:
            outputSTR = outputSTR + "1"
    return outputSTR




def hex2Bin(hexSTR):
    '''
    16 進位表示式轉為 2 進位表示式
    '''
    return bin(int(hexSTR, 16))[2:].zfill(len(hexSTR) * 4)
            
        
    


if __name__== "__main__":
    condition00X = "010111001010100001100011"
    condition00Y = "010000110001011100101001"

    condition01 = condNOT(condition00X)
    print("condition01 = ",condition01)
    condition02 = condAND(condition00X,condition00Y)
    print("condition02 = ",condition02)
    condition03 = condOR(condition00X,condition00Y)
    print("condition03 = ",condition03)
    condition04 = condXOR(condition00X,condition00Y)
    print("condition04 = ",condition04)
    
    b = hex2Bin("99")
    print("b(99) = ",b)
    c = hex2Bin("FF")
    print("c(FF) = ",c)
    d = hex2Bin("00")
    print("d(00) = ",d)
    e = hex2Bin("33")
    print("e(33) = ",e)
    print("====我是分隔線====")


    print("Ans:")
    Ans4Ch4P4_3a = condOR(b,b)
    print("Ch4P4_3a = ",Ans4Ch4P4_3a)
    Ans4Ch4P4_3b = condOR(b,d)
    print("Ch4P4_3b = ",Ans4Ch4P4_3b)
    Ans4Ch4P4_3c = condOR(b,c)
    print("Ch4P4_3c = ", Ans4Ch4P4_3c)
    Ans4Ch4P4_3d = condOR(c,c)
    print("Ch4P4_3d = ",Ans4Ch4P4_3d)
    print("====我是分隔線====")
    
    Ans4Ch4P4_4a = condNOT(condOR(b,b))
    print("Ch4P4_4a = ",Ans4Ch4P4_4a)
    Ans4Ch4P4_4b  = condOR(b,condNOT(d))
    print("Ch4P4_4b = ",Ans4Ch4P4_4b)
    Ans4Ch4P4_4c = condOR(condAND(b,e),condAND(d,c))
    print("Ch4P4_4c = ",Ans4Ch4P4_4c)
    Ans4Ch4P4_4d = condAND(condOR(b,e),condOR(d,c))
    print("Ch4P4_4d = ",Ans4Ch4P4_4d)
    
    print("====我是分隔線====")
    print("Ch4P4_13a = 0000 0100 1010 0000 ( 1184)" )
    print("Ch4P4_13b = 1111 1100 1010 0010 (-862 )" )
    print("Ch4P4_13c = 0000 0011 0101 1110 ( 862 )"  )
    print("Ch4P4_13d = 1111 1011 0110 0000 (-1184)")
    
   
    print("====我是分隔線====")
    print("Ch4P4_15a = 1000 1001 (-119(overflow)   )")
    print("Ch4P4_15b = 1011 0111 (-73(non-overflow))")
    print("Ch4P4_15c = 0100 1001 ( 73(non-overflow))")
    print("Ch4P4_15d = 0111 0111 ( 119(overflow)   )")
    
    print("====我是分隔線====")
    print("Ch4P4_16a = 0000 1111 0101 0001  (0F51)")
    print("Ch4P4_16b = 0000 1111 0010 1010  (0F2A)")
    print("Ch4P4_16c = 1000 0000 0001 0010  (8012)")
    print("Ch4P4_16d = 0111 1111 0101 0001  (7F51(overflow))")