# !/usr/bin/env python3
#  -*- coding:utf-8 -*-

#Python 程式的頭兩行一定是長這樣子。請花點力氣記一下。

def bin2int(N):
    i = 0
    n = 0
    while N>0:
        remain=int(N%10)
        n+=(remain)*(2**i)
        N=int(N//10)
        i+=1
    return n
if __name__ == "__main__":
    N = int(input("Enter Binary Number:"))
    print(bin2int(N))


 #   print (bin2int(N))

#p2-19a. 10
#p2-19b. 17
#p2-19c. 6
#p2-19d. 8

#p2-22a. 14
#p2-22b. 8
#p2-22c. 13
#p2-22d. 4

#p2-22a. 00010001 11101010 00100010 00001110
#P2-22b. 00001110 00111000 11101010 00111000
#P2-22c. 01101110 00001110 00111000 01001110
#P2-22d. 00011000 00111000 00001101 00000111

#p3-28a. 234
#p3-28b. 560
#p3-28c. 874
#p3-28d. 888

#p3-30a. 235
#p3-30b. 561
#p3-30c. 875
#p3-30d. 889

