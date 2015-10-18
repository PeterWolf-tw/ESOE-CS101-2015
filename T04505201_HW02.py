#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#Python 程式的前兩行是固定的，不能有其它的東西佔到這兩行，請牢記。

def int2bin(N):
    '''
    本函式將 int 整數轉為 bin 二進位制表示
    '''
    s=N
    tmpLIST = []
    while N > 0:
        remainder = int(N % 2)
        tmpLIST.append(remainder)
        N = (N - remainder) / 2
    tmpLIST.append(0)

    ans = ""
    for j in tmpLIST[::-1]: #將 tmpLIST 中的數字從尾至頭傳入 j
        ans = ans + str(j)
    print ("{0} 的二進位表示為 {1}.".format(s, ans))
    return None

def bin2int(N):
    number=int(N)
    length=len(N)
    n=0
    for i in range(length):
        n+=number%10*(2**i)
        number=int(number/10)
    print ("{0} 的十進位表示為 {1}.".format(N, n))
    return None

if __name__ == '__main__':
    intNumber = 560
    int2bin(intNumber)
    binNumber = "01100101"
    bin2int(binNumber)
    print("please input another binary number:")
    num=input()
    bin2int(num)

#2-19:a. 10位 b. 17位 c. 6位  d. 8位
#2-20:a. 14位 b. 8位  c. 13位 d. 4位
#2-22:a. 00010001 11101010 00100010 00001110
#     b. 00001110 00111000 11101010 00111000
#     c. 01101110 00001110 00111000 01001110
#     d. 00011000 00111000 00001101 00001011
#3-28: a.234  b.560  c.874  d.888
#3-30: a.234  b.560  c.875  d.889




