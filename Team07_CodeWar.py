#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#Assignment_Team01_HW05
#設計一個程式
#若使用者輸入一個數值
#可算出該數值所具有的所有公因數
#例如輸入633
#可得1 3 211 633
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
def Team04solution(input):
    return resultLIST
#Assignment_Team05_HW05
def Team05solution(input):
    return resultLIST
#Assignment_Team06_HW05
def Team06solution(input):
    return resultLIST
#Assignment_Team07_HW05
def Team07solution(input):
    return resultLIST
#Assignment_Team08_HW05
def Team08solution(input):
    return resultLIST
#Assignment_Team09_HW05
def Team09solution(input):
    return resultLIST
#Assignment_Team10_HW05
def Team10solution(input):
    return resultLIST
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
def Team14solution(input):
    return resultLIST
if __name__ == "__main__":
    testNUM01 = 633
    result = Team01solution(testNUM01)
    print(result)
    testSTR01 = "Hello"
    result = Team02solution(testSTR01)
    print(result)
    