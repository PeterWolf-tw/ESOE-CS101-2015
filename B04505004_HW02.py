# !/usr/bin/env python3
#  -*- coding:utf-8 -*-
# input限制為任何以二進為表示的整數
# 若輸入非二進位數，也將得到一個值



decimal = 0
value = 1
k = 10 


binary = int(input("Enter Binary Number:"))

while(binary > 0):
    remainder = (binary % k) 
    if(remainder > 0):
        decimal += value
    k *= 10
    binary -= remainder
    value *= 2 
print (decimal)
