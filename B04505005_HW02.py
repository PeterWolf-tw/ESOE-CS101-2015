# !/usr/bin/env python3
#  -*- coding:utf-8 -*-

<<<<<<< HEAD
print ("test")

def bin2int(N):
    L=len(str(N))
    a=str(N)
    s=0
    
    for i in range(0,L):
        n= int (a[i])*(2**(L-1))
        L = L-1
        s=s+n
       
    return s    
        
if __name__ == '__main__':
    x= 11100101
    ans=bin2int(x)
    print(ans)
=======
#第一題呢？
>>>>>>> 828b1fb01d6f3d0653f3175597200464227c977e


#第二題
# p2-19 a=  10
# p2-19 b=  17
# p2-19 c=  6
# p2-19 d=  8

#第三題
# p2-20 a=  14
# p2-20 b=  8
# p2-20 c=  13
# p2-20 d=  4

#第四題
# p2-22 a=  00010001  11101010  00100010  00001110
# p2-22 b=  00001110  00111000  11101010  00111000
# p2-22 c=  01101110  00001110  00111000  01001110
# p2-22 d=  00011000  00111000  00001101  00001011

#第五題
# p3-28 a=  234
# p3-28 b=  560
# p3-28 c=  874
# p3-28 d=  888

#第六題
# p3-30 a=  234
# p3-30 b=  560
# p3-30 c=  875
# p3-30 d=  889