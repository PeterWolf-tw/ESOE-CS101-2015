#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#Python 程式的前兩行是固定的，請牢記。

def b2i(c):
   if c>=0:
      g=c
   else:
      g=-c

   a = 0
   i = 0
   while g>= 1:

      s = g%10
      a = s*(2**i) +a
      i = i+1
      g = g//10
   return a

d = ("Please enter a binary number:")
c = input(d)
c = int(c)
#Python 的縮排固定縮四格空格。
if c>=0:
 u = b2i(c)
else:
   u=-b2i(c)

print("The decimal number of" ,c,"is",u)





#2-19
# a 10
# b 17
# c 6
# d 8
#2-20
# a 14
# b 8
# c 13
# d 4
#2-22
# a 00001001 11101010 00100010 00001110
# b 00001110 00111000 11101010 00111000
# c 01101110 00001110 00111000 01001110
# d 00011000 00111000 00001101 00001011
#3-28
# a 765 #錯
# b 439 #錯
# c-874 #錯
# d-888 #錯
#3-30
# a 766 #錯
# b 440 #錯
# c-875 #錯
# d-889 #錯
