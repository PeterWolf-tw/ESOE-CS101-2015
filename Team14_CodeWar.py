#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import math

#team01
def divisorGenerator(n):
    resultlist = []
    
    for i in range(1,n+1):
        if n%i == 0:
            resultlist.append(i)
            
        else:
            continue
    return resultlist

if __name__ == "__main__":
    Ans01=divisorGenerator(100)
    print(Ans01)
    
    
    
#team02
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def piglatintranslator(enter_a_word):

    letterlist=[]

    if len(enter_a_word)>1:
        letterlist = list(enter_a_word)
    else:
        print("valid word! Dumbo!")
    print("".join(letterlist[1:]) + letterlist[0] + "ay")
    return letterlist




if __name__ == "__main__": 
    piglatintranslator("test")
    
    
#team03(pending)


#team04
def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

if __name__ == "__main__":
    print (fib(6))
    
    
#team05(pending)


#team06
def mean(numbers):
    return sum(numbers)*1.0/len(numbers)

def stanDev(numbers):
    
    length = len(numbers)
    
    m = mean(numbers)
    
    total_sum = 0
    
    for i in range(length):
        total_sum += (numbers[i]-m)**2
    
    under_root = float(total_sum)/length

    return math.sqrt(under_root)

if __name__== "__main__":
    numbers = [4,6,7,22]
    print(stanDev(numbers))
    
#team10
print("0  0  0  0  0  0  0  0  0  0")
print("0  1  2  3  4  5  6  7  8  9")
print("0  2  4  6  8 10 12 14 16 18")
print("0  3  6  9 12 15 18 21 24 27")
print("0  4  8 12 16 20 24 28 32 36")
print("0  5 10 15 20 25 30 35 40 45")
print("0  6 12 18 24 30 36 42 48 54")
print("0  7 14 21 28 35 42 49 56 63")
print("0  8 16 24 32 40 48 56 64 72")
print("0  9 18 27 36 45 54 63 72 81")
    