#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#team01
def e(x):
    a = []
    for i in range(1,x+1):
        if x%i == 0:
            a.append(i)
    return a
if __name__ == '__main__':
    d=int(input("in put a number:") ) 
    print(e(d))
    
#team02
def Pig(word):
    fixword = word.isalpha()   
    if fixword == True:
        x = word[0]
        y = len(word)
        word1 = word[1:y]
        word1 = word1 + x + 'ay'
        return word1
    else:
        return ('invalid word')
 
word = input('Please enter an English word: ')
print(Pig(word))

#team04
def term():
    n = int(input("what is the number of term?"))
    if n < 1:
        t = [0,1,1]
    for i in range(n+1):
        if i > 2:
            t.append(t[i-2]+t[i-1])
    if n >= 0:
        print(t[n])
        
#team05
def faq(xdata,ydata):
    xa=sum(xdata)/len(xdata)
    ya=sum(ydata)/len(ydata)
    s1=0

    for i in xdata:
        s1=s1+(i-xa)**2
    s2= 0
    for j in ydata:
        s2 =s2+(j-ya)**2
    a0 = 0
    for k in range(len(xdata)):
        a0 = a0 + (xdata[k]-xa)*(ydata[k]-ya)
    a = a0/(s1)
    b = (-(xa)*a+ya)
    print("y = ",round(a,4),"x + ",round(b,4))

#team06
def ans():
    sumx= 0
    nu = len(x)
    a = 0
    for i in range(nu) :
        x[i] = int(x[i])
        sumx = sumx + x[i]
    xa = sumx / nu
    for i in range(nu) :
        x[i] = int(x[i])
        a += ( x[i] - xa )**2 
    sd = ( a / nu )**(1/2)
    return sd 
