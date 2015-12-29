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
    