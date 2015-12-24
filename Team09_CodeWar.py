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

while n > 3 :
    LIST2.append(LIST2[-1]+LIST2[-2])
    if len(LIST2)==n:
        break
    if n < 3 :
        LIST2 = [1,1,2]
print (LIST2[n-1])



#Team06
#請輕鬆設計出一個可計算出任意個實數組之表準差的函數
# ex: input=(40,50,60) , output=8.164965809277....
# ex: input=(60,60,60,60) , output=0

score1 = []
import math
sore1 = [x for x in input("give me some numbers:").split()]
print (sore1)
average = sum(sore1)/len(sore1)
for n in range (0,len(sore1)-1):
    sore2 = []
    sore2.insert(n,sore1[n] - average)
    sore3 = []
    sore3.insert(n , sore2[n] * sore2[n])
    answer = math.sqrt(sum(sore3) / len(sore3))
    print (answer)
