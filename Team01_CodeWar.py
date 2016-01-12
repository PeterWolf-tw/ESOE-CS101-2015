#!/usr/bin/env python3
# -*- coding:utf-8 -*-2

#Team01

def aaa(x):
    a = []
    for i in range(1,x+1):
        if x%i == 0:
            a.append(i)
        else:
            continue
    b = []
    for j in a:
        b.append(j*-1)
    a.extend(b)
    return a
if __name__ == '__main__':
    c=int(input("請輸入一個數字:") ) 
    print(aaa(c))

#Team02

def jjj(x):
    y=list(x)
    y.append(y[0])
    y.remove(y[0])
    y.append("ay")
    z = ""
    for i in y :
        z = z + i
    return z
if __name__ == '__main__':
    a=input("請輸入一個英文單字:")
    print(jjj(a))

#Team06

def bbb(x):
    result = 0
    print(len(x),type(x))
    pupu = 0
    for i in range(len(x)):
        c[i] = int(c[i])
        pupu = pupu + c[i]
    avr = pupu /len(x)
    #print(avr)
   
    for i in range(len(x)):
        c[i]= int(c[i])
        result = result + (c[i]-avr)**2
    result = result / len(x)
    result = result ** 0.5
    return result
    
if __name__ == '__main__':
    c=list(input("請輸入一串數字:").split(",") ) 
    print(bbb(c))    

#Team7

def factorial(x):
    a=int(x)
    x=a
    while x >=2:
        a=a*(x-1)
        x-=1
    return a 
import itertools    
def permutation(y):
    i=list(str(y)) 
    j=list(itertools.permutations(i,x))
    g=""
    for i in j:
        g=g+" ".join(i)+"\n"
    return g
if __name__=="__main__":
    x=int(input("How many number do you want to permutate?"))
    n=factorial(x)
    y=input("Please enter all of the number you want to permutate without seperation.")
    o=permutation(y)
    print(n)
    print(o)
    

#Team10

def kkk():
    for i in range(0,10):
        for j in range(0,10):
            if i*j < 10:
                print(i*j,end='')
                print("  ",end='')
            else:
                print(i*j,end='')
                print(" ",end='')
        print('')
    return "九九乘法表"
if __name__ == '__main__':
    print(kkk())
                