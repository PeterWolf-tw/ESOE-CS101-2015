#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#請參考以下空白程式，能夠將輸入的字串定義為m進位法，並且換算成n進位法
#其中，m及n為任意輸入的數值，且是介於2至36的正整。而字串中的英文字母大小寫皆可運算

def m2n(x):
    '''
    本函式將 m 進位制表示數轉為 n 進位制
    '''    
    a = input("m = ")
    b = input("n = ")
      
if __name__ == "__main__":
   
    testSTR = "16ZEQBA"
    result = m2n(testSTR)
    print(result)
