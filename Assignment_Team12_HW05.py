#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#請參考以下空白程式，設計一支程式能將輸入的字串定義為m進位法，並且換算成n進位法(其中，m, n為介於2至62的正整數)
#在此，我們定義大寫英文字母A為10、Z為35;小寫英文字母a為36、z為62，其他字母以此類推
#可不考慮負數及浮點數的計算


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
