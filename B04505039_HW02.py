#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#Python 程式的前兩行是固定的，不能有其它的東西佔到這兩行，請牢記。

def bin2int(N):
    L = len(str(N))
    STR = str(N)
    Sum = 0
    a = 0

    while 0 < L :
        n = int(STR[a])*(2**int(L-1))
        L = L - 1
        a = a + 1
        Sum = Sum + n
    return Sum

if __name__ == '__main__':

    #我建議你使用一個 IDE 來編寫程式原始碼。你的程式裡的中文在我這裡看起來是一片亂碼！
    #x = input(" ��J�@�ӤG�i��� ")
    x = input("input")
    ans = bin2int(x)
    #print( x , "���Q�i��Ƭ�", ans )
    print( x , ans )




#p2.19
a. 10
b. 17
c. 6
d. 8



#p2.20
a. 14
b. 8
c. 13
d. 4



#p2.22
a. 00010001 11101010 00100010 00001110
b. 00001110 00111000 11101010 00111000
c. 01101110 00001110 00111000 01001110
d. 00011000 00111000 00001101 00001011


#p3.28
a. 234
b. 560
c. 874
d. 888



#p3.30
a. 234
b. 560
c. 985 #錯
d. 999 #錯