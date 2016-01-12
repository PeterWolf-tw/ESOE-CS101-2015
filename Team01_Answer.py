#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#設計一個程式
#若使用者輸入一個數值
#可算出該數值所具有的所有公因數
#例如輸入633
#可得1 3 211 633
#############################################
def factorize(n):
    factors=[]
    x=int(n)
    d=1
    while d >=1 and d <= x:
        a = x%d
        if a == 0:
            factors.append(d)
            factors.append(-d)
        d = d+1
        sorted(factors)
    return factors    
if __name__=="__main__":
    n=input("Please enter the number you want to factorize:")
    x=int(n)
    e=factorize(x)
    print(e)
##############Team01##################
#Team02:Half-Pass(只顯示正因數)
#Team03:Fail(無法執行，加了那兩行也一樣)
#Team04:Half-Pass(只顯示正因數)
#Team05:Pass
#Team06:Pass
#Team07:Half-Pass(只顯示正因數)
#Team08:Half-Pass(只顯示正因數)
#Team09:Half-Pass(只顯示正因數)
#Team10:我找不到你們的檔案？
#Team11:Pass
#Team12:Pass
#Team13:Pass
#Team14:Half-Pass(只顯示正因數)