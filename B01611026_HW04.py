#!/usr/bin/env python3
# -*- coding:utf-8 -*-

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
	for i in inputSTR_X and j in inputSTR_Y: #for-迴圈裡不會有兩個 index 條件。這程式無法運作。
		if i==j=="1":
			outputSTR="1"
		else:
			outputSTR="0"
    return outputSTR

#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
	outputSTR = ""
    for i in inputSTR_X and j in inputSTR_Y:
		if i|j=="1":
			outputSTR="1"
		else:
			outputSTR="0"
#condition00 xor condition04
def conXOR(inputSTR_X, inputSTR_Y):
	outputSTR = ""
    for i in inputSTR_X and j in inputSTR_Y:
		if i^j=="1":
			outputSTR="1"
		else:
			outputSTR="0"
    return


def hex2Bin(hexSTR):
    '''
    16 進位表示式轉為 2 進位表示式
    '''
    return bin(int(hexSTR, 16))[2:]


if __name__== "__main__":
    condition00X = "010111001010100001100011"
    condition00Y = "010000110001011100101001"

    condition01 = condNOT(condition00X)
    print(condition01)

    #可利用 hex2Bin() 函式計算十六進位表示式 "99" 的二進位表式：(範例如下)
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
    Ch4P4_15b = "-73"
    Ch4P4_15c = "73"
    Ch4P4_15d = "overflow"
    print("========")
    Ch4P4_16a = "0F51"
    Ch4P4_16b = "0F2A"
    Ch4P4_16c = "8012"
    Ch4P4_16d = "7F51"