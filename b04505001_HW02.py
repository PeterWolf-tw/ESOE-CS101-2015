# !/usr/bin/env python3
#  -*- coding:utf-8 -*-


#Python 的縮排都是空四個空格。下次請注意。
def GG(N):
 x=0
 if (N>=0):
      while (N>=x):
       x+=1
      k=x-1
 if (N<0):
     while (N<x):
      x-=1
     k=x
 return k

def bin2int(N):
 y=1
 z=0
 if (N<0):
          N*=-1
          while (N > 0):
               z+=(N/10-GG(N/10))*10*y
               N=GG(N/10)
               y*=2
          z*=-1
 else:
  while(N>0):
          z+=(N/10-GG(N/10))*10*y
          N=GG(N/10)
          y*=2
 return z

#你的程式沒有進入點 (如下), 以後請改進。
if __name__ == "__main__":
 print(bin2int(100))

#p2_19a=10
#p2_19b=17
#p2_19c=6
#p2_19d=8
#p2_20a=14
#p2_20b=8
#p2_20c=13
#p2_20d=4
#p2_22a=00010001 11101010 00100010 00001110
#p2_22b=00001110 00111000 11101010 00111000
#p2_22c=01101110 00001110 00111000 01001110
#p2_22d=00011000 00111000 00001101 00001011
#p3_28a=234
#p3_28b=560
#p3_28c=874
#p3_28d=888
#p3_30a=234
#p3_30b=560
#p3_30c=875
#p3_30d=889