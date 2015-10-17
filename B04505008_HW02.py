#!/usr/bin/env python3
# -*- coding:utf-8 -*-



#作業 1.
# 請參考上例，自己寫一個將二進位表示數轉為十進位制的函式：
def bin2int(N):
    '''
    本函式將 bin 二進位制表示數轉為 int 整數
    '''
a = 1
decimal = 0


binary = int(input("Enter Binary Number:"))

if(binary > 0):
    N =  binary
    while(N > 0):
        #Python 的縮排固定縮四格空格。
         remainder = (N % 10)
         if(remainder > 0):
            decimal += a
         a *= 2
         N=( N- remainder ) / 10

    print (decimal)

else:
    N =  -binary
    while(N > 0):
            remainder = (N % 10)
            if(remainder > 0):
               decimal += a
            a *= 2
            N=( N- remainder ) / 10

    print (0-decimal)








#作業 2. 課本 Ch2. P2.19
#       a.= 10
#       b.= 17
#       c.= 6
#       d.= 8
#作業 3. 課本 Ch2. P2.20
#       a.= 14
#       b.= 8
#       c.= 13
#       d.= 4
#作業 4. 課本 Ch2. P2.22
#       a.= 00010001 11101010 00100010 00001110
#       b.= 00001110 00111000 11101010 00111000
#       c.= 01101110 00001110 00111000 01001110
#       d.= 00011000 00111000 00001101 00001011
#作業 5. 課本 Ch3. P3.28
#       a.= 234
#       b.= 560
#       c.= 874
#       d.= 888
#作業 6. 課本 Ch3. P3.30
#       a.= 234
#       b.= 560
#       c.= 875
#       d.= 889
