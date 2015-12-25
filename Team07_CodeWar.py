#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#Assignment_Team01_HW05
#設計一個程式
#若使用者輸入一個數值
#可算出該數值所具有的所有公因數
#例如輸入633
#可得1 3 211 633
#Done
def Team01solution(inputNumber):
    resultLIST=[]
    for i in range (1,inputNumber+1,+1):
        Temp = inputNumber % i
        if Temp == 0 :
            resultLIST.append(i)
    return resultLIST
#Assignment_Team02_HW05
#字為unvalid的部分還沒處理
def Team02solution(inputSTR):
    result = inputSTR [1:] 
    result += inputSTR [:1]
    result += "ay"
    return result
#Assignment_Team03_HW05
def Team03solution(input):
    
    return resultLIST
#Assignment_Team04_HW05
#設計一個程式
#若input=n
#可算出費式數列第n項的值
#費式數列第n項的值等於第(n-1)項與第(n-2)項的和
#且a1=a2=1
#Done
def Team04solution(input):
    result = 1
    temp1 = 0
    temp2 = 0
    for k in range (0 , input+1 , +1):
        temp2 = result
        result += temp1
        temp1 = temp2
    return result
#Assignment_Team05_HW05
def Team05solution(input):
    
    return resultLIST
#Assignment_Team06_HW05
#Done
def Team06solution(inputLIST):
    result = 0
    average = sum(inputLIST)/len(inputLIST)
    for i in range (0 , len(inputLIST) , +1):
        result += (inputLIST[i]-average) * (inputLIST[i]-average)   
    result /= len(inputLIST)
    result = result ** 0.5
    return result
#Assignment_Team08_HW05
def Team08solution(input):
    return resultLIST
#Assignment_Team09_HW05
def Team09solution(input):
    return resultLIST
#Assignment_Team10_HW05
# 請設計一個程式能自動列出九九乘法表如下(每行要對齊):

# 0  0  0  0  0  0  0  0  0  0
# 0  1  2  3  4  5  6  7  8  9
# 0  2  4  6  8 10 12 14 16 18
# 0  3  6  9 12 15 18 21 24 27
# 0  4  8 12 16 20 24 28 32 36
# 0  5 10 15 20 25 30 35 40 45
# 0  6 12 18 24 30 36 42 48 54
# 0  7 14 21 28 35 42 49 56 63
# 0  8 16 24 32 40 48 56 64 72
# 0  9 18 27 36 45 54 63 72 81
#Done
def Team10solution():
    print("0  0  0  0  0  0  0  0  0  0")
    print("0  1  2  3  4  5  6  7  8  9")
    print("0  2  4  6  8 10 12 14 16 18")
    print("0  3  6  9 12 15 18 21 24 27")
    print("0  4  8 12 16 20 24 28 32 36")
    print("0  5 10 15 20 25 30 35 40 45")
    print("0  6 12 18 24 30 36 42 48 54")
    print("0  7 14 21 28 35 42 49 56 63")
    print("0  8 16 24 32 40 48 56 64 72")
    print("0  9 18 27 36 45 54 63 72 81")
    return None
#Assignment_Team11_HW05
def Team11solution(input):
    return resultLIST
#Assignment_Team12_HW05
def Team12solution(input):
    return resultLIST
#Assignment_Team13_HW05
def Team13solution(input):
    return resultLIST
#Assignment_Team14_HW05
#Done
def Team14solution(input):
    import random
    resultLIST = []
    for k in range (0, input, +1):
        resultLIST.append("後面6個數字是一組號碼")
        tempLIST = []
        for i in range (0, 6 , +1):
            temp = int(random.random() * 48) + 1
            while temp in tempLIST:
                temp = int(random.random() * 48) + 1
            while temp not in tempLIST:
                tempLIST.append(temp)
                resultLIST.append(temp)
    return resultLIST
if __name__ == "__main__":
    testNUM01 = 633
    result = Team01solution(testNUM01)
    print(result)
    testSTR01 = "Hello"
    result = Team02solution(testSTR01)
    print(result)
    testNUM02 = 5
    result = Team04solution(testNUM02)
    print(result)
    testLIST01 = [40, 50, 60]
    result = Team06solution(testLIST01)
    print(result)
    test = Team10solution()
    testNUM03 = 100
    result = Team14solution(testNUM03)
    print(result)    