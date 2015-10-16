# !/usr/bin/env python3
#  -*- coding:utf-8 -*-



decimal = 0
value = 1


binary = int(input("Please enter a binary number:"))

if(binary > 0):
    x =  binary
    while(x > 0):        
         remainder = (x % 10) 
         if(1 >= remainder >= 0):
              decimal += remainder * value
         else:
             print("Oh,no!God is sad to say this is not a binary number.")
             import sys
             sys.exit() 
         x = x // 10
         value *= 2 
    print ("The value of the input is:",decimal)
         

else: 
    x = - binary
    while(x > 0):
        remainder = (x % 10) 
        if(1 >= remainder >= 0):
              decimal += remainder * value
        else:
            print("Oh,no!God is sad to say this is not a binary number.")
            import sys
            sys.exit()
        x = x // 10
        value *= 2
    print ("The value of the input is:",-decimal) 



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
