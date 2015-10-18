# !/usr/bin/env python3
#  -*- coding:utf-8 -*-

#Python 程式的頭兩行一定是長這樣子。請花點力氣記一下。

#encoding: utf-8
def bin2int(N):
    j=len(N)
    L=N[1:j-1]
    #print int(L,2)
    #從 Python3 開始 print() 成為一個 function()，所以要加上括號。
    print(int(L, base=2))

if __name__ == '__main__':
    binNumber = "01100101"

    bin2int(binNumber)
    #你的 bin2int() 算出來的答案不正確哦！


'''
課本題目答案
2-19
    a. 10
    b. 17
    c. 6
    d. 8

2-20
    a. 14
    b. 8
    c. 13
    d. 4

2-22
    a. 00010001 11101010 00100010 00001110
    b. 00001110 00111000 11101010 00111000
    c. 01101110 00001110 00111000 01001110
    d. 00011000 00111000 00001101 00001011

3-28
    a. 234
    b. 560
    c. 874
    d. 888

3-30
    a. 234
    b. 560
    c. 875
    d. 889
    '''