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
LIST3 = []
import math
LIST3 = [x for x in input("give me some numbers:").split()]
print (LIST3)
average = sum(LIST3)/len(LIST3)
for n in range (0,len(LIST3)-1):
    LIST4 = []
    LIST4.insert(n,LIST3[n] - average)
    LIST5 = []
    LIST5.insert(n , LIST4[n] * LIST4[n])
    answer = math.sqrt(sum(LIST5) / len(LIST5))
    print (answer)



#Team09
import random
LIST = [0,1,2,3,4,5,6,7,8,9]
print (random.sample (LIST , 4))

x = 0

def inputTest():
    x = input(">>> Input: ")
    print (x)

while (True):
    inputTest()
    
# 請設計一個程式能自動列出九九乘法表如下(每行要對齊):
    
# 0  0  0  0  0  0  0  0  0  0
# 0  1  2  3  4  5  6  7  8  9
# 0  2  4  6  8 10 12 14 16 18
# 0  3  6  9 12 15 18 21 24 27
# 0  4  8 12 16 20 24 28 32 36
# 0  5 10 15 20 25 30 35 40 45
# 0  6 12 18 24 30 36 42 48 54
# 0  7 14 21 28 35 42 49 56 63
# 0  8 16 24 32 40 48 56 64 72
# 0  9 18 27 36 45 54 63 72 81

def team10():
    for i in range(0,10):
        for j in range(0,10):
            if i*j < 10 :
                print(i*j, end='')
                print('  ', end='')
            else :
                print(i*j, end='')
                print(' ', end='')
        print('')
      
    return ''
    
if __name__== "__main__":
    print("team10:")
    t10 = team10()
    print(t10)
    
    
    
    
