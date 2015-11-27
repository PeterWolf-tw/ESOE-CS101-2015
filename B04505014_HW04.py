#!/usr/bin/env python 3
#-*- coding:utf-8 -*-

#這兩行不要漏了

def condAND(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for i,j in zip(inputSTR_X,inputSTR_Y):

        if set(i)&set(j)=={"1"}:
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
    return outputSTR







def condOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for i,j in zip(inputSTR_X,inputSTR_Y):

        if set(i)&set(j)=={"0"}:
            outputSTR = outputSTR + "0"
        else:
            outputSTR = outputSTR + "1"
    return outputSTR








def condXOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for i,j in zip(inputSTR_X,inputSTR_Y):

        if if a == b :
            outputSTR = outputSTR + "0"
        else:
            outputSTR = outputSTR + "1"
    return outputSTR











def hex2Bin(hexSTR):
    '''
    16 �i���ܦ��ର 2 �i���ܦ�
    '''
    return bin(int(hexSTR, 16))[2:]


if __name__ == '__main__':
    condition00X = "010111001010100001100011"
    condition00Y = "010000110001011100101001"

    condition01 = condNOT(condition00X)
    print(condition01)

    #�i�Q�� hex2Bin() �禡�p��Q���i���ܦ� "99" ���G�i������G(�d�Ҧp�U)
    b = hex2Bin("99")
    print(b)


    print("Ans:")
    Ch4P4_3a = "10011001"
    Ch4P4_3b = "11111111"
    Ch4P4_3c = "10011001"
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
    Ch4P4_15b = "no overflow"
    Ch4P4_15c = "no overflow"
    Ch4P4_15d = "overflow"
    print("========")
    Ch4P4_16a = "0F51"
    Ch4P4_16b = "0F2A"
    Ch4P4_16c = "8012"
    Ch4P4_16d = "7F51"