#!/usr/bin/env python 3
#-*- coding:utf-8 -*-

def int2bin(N):
    '''
    本函式將 int 整數轉為 bin 二進位制表示
    '''
    tmpLIST = []
    while N > 0:
        remainder = int(N % 2)
        tmpLIST.append(remainder)
        N = (N - remainder) / 2
    tmpLIST.append(0)

    ans = ""
    for j in tmpLIST[::-1]: #將 tmpLIST 中的數字從尾至頭傳入 j
        ans = ans + str(j)
    print("{0} 的二進位表示為 {1}.".format(intNumber, ans))
    return None

if __name__ == '__main__':
    intNumber = 100
    
    int2bin(intNumber)

    binNumber = "01100101"
    #bin2int(number)