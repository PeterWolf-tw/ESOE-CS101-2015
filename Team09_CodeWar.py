#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#Team01
#設計一個程式
#若使用者輸入一個數值
#可算出該數值所具有的所有公因數
#例如輸入633
#可得1 3 211 633


x=int(input("please enter a number: "))
#print (x)
LIST1 = []

import math
a = int(math.sqrt(x))
#print (a)

i=1
for i in range(1, a+1) :
    if x % i == 0:
        LIST1.append(i)
        if x//i not in LIST1:
            LIST1.append(x//i)
        
        #print (LIST1)
        i = i+1
        continue
    else:
        i = i+1
        continue
LIST1.sort(reverse=False)

print (LIST1)




#Team04
#設計一個程式
#若input=n
#可算出費式數列第n項的值
#費式數列第n項的值等於第(n-1)項與第(n-2)項的和
#且a1=a2=1

LIST2 = []
LIST2.insert(0,1)
LIST2.insert(1,1)
LIST2.insert(2,2)

n=int(input("please enter a number: "))

while True :
    LIST2.append(LIST2[-1]+LIST2[-2])
    if len(LIST2)==n:
        break
print(LIST2[-1])

    


    
    
    
    
    
    
