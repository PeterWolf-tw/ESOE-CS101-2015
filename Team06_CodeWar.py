Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #!/usr/bin/env python3
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
          
#Team03
class Friends:
    def __init__(self, connections):
        self.connections = connections
    
    
    def names(self):
        setA = set()
        for i in self.connections:
            setA = setA | i
        return setA

    def connected(self, connections):
        setB = set()
        for i in self.connections:
            if connections in i:
                setB = setB | i
        setB = setB - set(connections)
        return setB
#Team04
def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

if __name__ == "__main__":
    print (fib(6))
    
#Team06

import statistics
statistics.stddev([x,y,z])
    

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

#Team11
def team11(a):
    import random
    fuck = [(1, 'p1'), (2, 'p2'), (3, 'p3'), (4, 'p4'), (5, 'p5')]
    for i in range(5,0,-1):
        if i>a:
            fuck.remove(fuck[i-1])
    yee = 0
    key = random.randint(1, 36)
    king = random.randint(1, a)
   
    while(yee < key ):
        for i in fuck:
            print(i[1], end=',')
            if i == fuck[king-1]:
                print(key, end=',')
                print(yee, end=',')
            yee = yee + int(input())
            if yee >= key :
                b= i[1]
                break
    print(b, end = '')
    print(" lose")
    return ''

#Team14
def lottery(n):
    import random
    for i in range(0,n) :
        j=0
        result = []
        while(j != 6):
            srand = random.randint(1, 49)
            if srand not in result:
                result.append(srand)
                j += 1
        result.sort()                    
        print(result)   
    return ""
