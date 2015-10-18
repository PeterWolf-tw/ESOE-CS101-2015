#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def bin2int(N):
    x = 0
    a = 0
    b = -1
    while N>= 1:
        r = N%10
        x = r*(pow(2,a)) + x
        a += 1
        N = N//10
    return x
#你在第 12 行就做了 return。一個 function() 一旦走到 return 這一步，以下的就不會做囉！
#也就是說，你從 15 行開始到 20 行之間的程式都白寫了呢。
    while 1>N>=0:
        r = N*10
        x = r*(pow(2,b)) + x
        b -= 1
        N = N*10 - int(N*10)    
    return x
c = ("please input a number:")
N = input(c)
N = int(N)
x = bin2int(N)
print(x)
    

# p2-19 a=10
# p2-19 b=17
# p2-19 c=6
# p2-19 d=8
# p2-20 a=14
# p2-20 b=8
# p2-20 c=13
# p2-20 d=4
# p2-22 a=00010001 11101010 00100010 00001110
# p2-22 b=00001110 00111000 11101010 00111000
# p2-22 c=01101110 00001110 00111000 01001110
# p2-22 d=00011000 00111000 00001101 00001011
# p3-28 a=234
# p3-28 b=560
# p3-28 c=874
# p3-28 d=888
# p3-30 a=234
# p3-30 b=560
# p3-30 c=875
# p3-30 d=889