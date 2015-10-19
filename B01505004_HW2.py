#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#Python 程式的前兩行是固定的，請牢記。

def bin2int(N):
    a=1
    ans=0
    while (N > 0):

        remainder = N % 10
        if (remainder>0):
            ans+=a
        a*=2
        N = (N - remainder) / 10
    return ans

if __name__ == '__main__':

    binNumber = 1010
    bin2int(binNumber)
    print(bin2int(binNumber))
    #你可以用一個變數來承接 bin2int() 的 return。像這樣：
    # x = bin2int(binNumber)
    # print(x)


#2. a.= 10  b.= 17  c.= 6  d.= 8

#3. a.= 14  b.= 8   c.= 13 d.= 4

#4.  a.= 00010001 11101010 00100010 00001110
#    b.= 00001110 00111000 11101010 00111000
#    c.= 01101110 00001110 00111000 01001110
#    d.= 00011000 00111000 00001101 00001011


#5. a.= 234  b.= 560  c.= 874 d.= 888

#6. a.= 234  b.= 560  c.= 875  d.= 889

