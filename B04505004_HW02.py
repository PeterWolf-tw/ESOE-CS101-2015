# !/usr/bin/env python3
#  -*- coding:utf-8 -*-
# input限制為任何以二進位表示的正整數
# 若輸入非二進位數，也將得到一個值



decimal = 0
value = 1
k = 10 


binary = int(input("Enter Binary Number:"))

if(binary > 0):
    x =  binary
    while(x > 0):        
         remainder = (x % k) 
         if(remainder > 0):
              decimal += value
         k *= 10
         x -= remainder
         value *= 2 
    print (decimal)

else: 
       x = - binary
       while(x > 0):
        remainder = (x % k) 
        if(remainder > 0):
              decimal += value
        k *= 10
        x -= remainder
        value *= 2
       print (0 - decimal) 



# p2-19a=   10
# p2-19b=   17
# p2-19c=   6
# p2-19d=   8
# p2-20a=   14
# p2-20b=   8
# p2-20c=   13
# p2-20d=   4
# p2-22a=  00010001  11101010  00100010  00001110
# p2-22b=  00001110  00111000  11101010  00111000
# p2-22c=  01101110  00001110  00111000  01001110
# p2-22d=  00011000  00111000  00001101  00001011
# p3-28a=   234
# p3-28b=   560
# p3-28c=   874
# p3-28d=   888
# p3-30a=   234
# p3-30b=   560
# p3-30c=   875
# p3-30d=   889
