#!/usr/bin/env python3
# -*- coding:utf-8 -*

def bin2int(N):

    N = str(binN)
    L = len(N)
    k = 0
    t = L-1
    i = 1
    x = 0

    while i <= L :
        a = N[k]
        x += pow(2,t)*int(a)
        k += 1
        i += 1
        t -= 1
    print(str(N) + " 的十進位為 " + str(x) )

    return None

if __name__ == '__main__':
    binN = input("請輸入一個二進位數: ")

    bin2int(binN)

#Good job.

#2-19
#a. 10
#b. 17
#c. 6
#d. 8

#2-20

#a. 14
#b. 8
#c. 13
#d. 4

#2-22
#a. 00010001 11101010 00100010 00001110
#b. 00001110 00111000 11101010 00111000
#c. 01101110 00001110 00111000 01001110
#d. 00011000 00111000 00001101 00001011

#3-28
#a. 234
#b. 560
#c. 874
#d. 888

#3-30
#a. 234
#b. 560
#c. 875
#d. 889




