#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def bin2int(N):
    aa,k,s=0,0,0
    while N>0:
        k=N%10
        if k!=0 or k!=1:
            print ('This is Not a Binary')
            return None
        s+=k*(2**aa)
        N=N//10
        aa+=1
    print(s)
    return None

if __name__ == '__main__':
    print('input a binary')
    bin2int(int(input()))


#2. a.= 10  b.= 17  c.= 6  d.= 8

#3. a.= 14  b.= 8   c.= 13 d.= 4

#4.
#a.= 00010001 11101010 00100010 00001110
#b.= 00001110 00111000 11101010 00111000
#c.= 01101110 00001110 00111000 01001110
#d.= 00011000 00111000 00001101 00001011


#5. a.= 234  b.= 560  c.= 874 d.= 888

#6. a.= 234  b.= 560  c.= 875  d.= 889


