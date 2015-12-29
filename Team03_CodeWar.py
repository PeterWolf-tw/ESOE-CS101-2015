#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#team01
>>> def divisor(n):
    resultLIST=[]
    for i in range(1,n+1):
        if n%i==0:
            resultLIST.append(i)
            return resultLIST

#team02
#if __name__ == '__main__':
    x = str(input("input a English word:"))
    if x.isalpha() == True:
        print(x)
        print(x[0])
        x = list(x)
        x.append(x[0])
        x.remove(x[0])
        x.extend(['a','y','.'])
        print(str(x))
        n = len(x)
        y = ""
        for i in range(n):
            print(x[i])
            y = y + x[i]
        print(y)

    else:
        print("it is not a English word")
#team03
from itertools import chain


class Friends:
    def __init__(self, connections):
        self.connections = list(connections)



    def names(self):
        return set(chain(*self.connections))

    def connected(self, name):
        neighbors = []
        [neighbors.extend(list(i)) for i in self.connections if name in i]
        neighbors = set(neighbors)
        if name in set(neighbors):
            neighbors.remove(name)
        return neighbors


>>> #team04
>>> def feynman(n):
    number=0
    a=1
    b=1
    if n>2:
        a=b
        b=a+b
        n=n-1
        number=b
        return number
    else:
        number=b
        return number

#team05	
def team05 (xdata,ydata) :


    #xdata = int(xdata)
    #print(xdata,type(xdata))
    xdata = list(xdata)
    #print(xdata,type(xdata))
    #print(xdata[0])

    kobe = 0
    lenxdata = len(xdata)

    #print(type(lenxdata))
    for i in range(lenxdata) :
        #print(type(xdata[0]))
        xdata[i] = int(xdata[i])
        kobe = kobe + xdata[i]
    sumxdata = kobe
    xbar = sumxdata / lenxdata
    sumxminxbar = 0


    ydata = list(ydata)
    lenydata = len(ydata)

    wade = 0
    for i in range(lenydata)  :
        ydata[i] = int(ydata[i])
        wade = wade + ydata[i]
        sumydata = wade 
    ybar = sumydata / lenydata




    for i in range(lenxdata) :
        b = (xdata[i] - xbar)**2
        sumxminxbar = sumxminxbar + b


    ##for i in range(lenydata) :
        ##c = (ydata[i] - ybar)**2
        ##sumyminybar = sumyminybar + c
    ##print(sumxminxbar)
    ##print(sumyminybar)
    a = 0

    for i in range(lenxdata)  :
        d = (xdata[i]-xbar) * (ydata[i]-ybar)
        a = a + d 
    ##print(a)

    m = a / sumxminxbar 
    c = ybar - m *xbar
    if c > 0 :
        ans = print("回歸直線為: y=",m,"x","+",c)
    else :
        ans = print("回歸直線為: y=",m,"x",c) 


if __name__ == '__main__':
    xdata =  input("請輸入xdata的值(中間以逗號隔開):").split(",")
    ydata =  input("請輸入ydata的值(中間以逗號隔開):").split(",")
    print(team05(xdata, ydata))	

#team06

def team06(x) :

    sumx= 0
    lenx = len(x)
    kobe = 0
    for i in range(lenx) :
        x[i] = int(x[i])
        sumx = sumx + x[i]
    xbar = sumx / lenx
    #print(xbar)
    for i in range(lenx) :
        x[i] = int(x[i])
        kobe += ( x[i] - xbar )**2 
    wade = ( kobe / lenx )**(1/2)
    return wade 
if __name__ == '__main__':
    Lebron = input().split(",")
    print(team06(Lebron))


#team07
#if __name__ == '__main__':
    x = int(input("input a number from 1 to 10 : "))
    l = input("input some numbers").split(",")
    if len(l) != x:
        print("erro!!!")
    y = 1
    a = x + 1
    for i in range(a):
        #print(i)
        if i != 0 :
            y = y * i
        else:
            y = 1
    print(y)

    if x == 1:
        print(l[0])

    elif x == 2:
        for i in l:
            if i != 0:
                for j in l:
                    if j != 0:
                        if i != j :
                            print(i,j)


    elif x == 3:

        for i in l:
            if i != 0:
                for j in l:
                    if j != 0:
                        for k in l:
                            if k != 0:
                                if i != j :
                                    if j != k:
                                        if i != k:
                                            print(i , j , k)
    elif x == 4:
        for i in l:
            if i != 0:
                for j in l:
                    if j != 0:
                        for k in l:
                            if k != 0:
                                for m in l:
                                    if i!=j and i!=k and i!=m and j!=k and j!=m and k!=m:
                                        print(i,j,k,m)

    elif x == 5:
        for i in l:
            for j in l:
                for k in l:
                    for m in l:
                        for n in l:
                            if i!=j and i!=k and i!=m and j!=k and j!=m and k!=m and i!=n and j!=n and k!=n and m!=n:
                                print(i,j,k,m,n)


    elif x == 6:
        for i in l:
            for j in l:
                for k in l:
                    for m in l:
                        for n in l:
                            for o in l:
                                if i!=j and i!=k and i!=m and j!=k and j!=m and k!=m and i!=n and j!=n and k!=n and m!=n and i!=o and j!=o and k!=o and m!=o and n!=o:
                                    print(i,j,k,m,n,o)

    elif x == 7:
        for i in l:
            for j in l:
                for k in l:
                    for m in l:
                        for n in l:
                            for o in l:
                                for p in l:
                                    if i!=j and i!=k and i!=m and j!=k and j!=m and k!=m and i!=n and j!=n and k!=n and m!=n and i!=o and j!=o and k!=o and m!=o and n!=o and i!=p and j!=p and k!=p and m!=p and n!=p and o!=p:
                                        print(i,j,k,m,n,o,p)

    elif x == 8:
        for i in l:
            for j in l:
                for k in l:
                    for m in l:
                        for n in l:
                            for o in l:
                                for p in l:
                                    for q in l:
                                        if i!=j and i!=k and i!=m and j!=k and j!=m and k!=m and i!=n and j!=n and k!=n and m!=n and i!=o and j!=o and k!=o and m!=o and n!=o and i!=p and j!=p and k!=p and m!=p and n!=p and o!=p and i!=q and j!=q and k!=q and m!=q and n!=q and o!=q and p!=q:
                                            print(i,j,k,m,n,o,p,q)


    elif x == 9:
        for i in l:
            for j in l:
                for k in l:
                    for m in l:
                        for n in l:
                            for o in l:
                                for p in l:
                                    for q in l:
                                        for r in l:
                                            if i!=j and i!=k and i!=m and j!=k and j!=m and k!=m and i!=n and j!=n and k!=n and m!=n and i!=o and j!=o and k!=o and m!=o and n!=o and i!=p and j!=p and k!=p and m!=p and n!=p and o!=p and i!=q and j!=q and k!=q and m!=q and n!=q and o!=q and p!=q and i!=r and j!=r and k!=r and m!=r and n!=r and o!=r and p!=r and q!=r:
                                                print(i,j,k,m,n,o,p,q,r)

    elif x == 10:
        for i in l:
            for j in l:
                for k in l:
                    for m in l:
                        for n in l:
                            for o in l:
                                for p in l:
                                    for q in l:
                                        for r in l:
                                            for s in l:
                                                if i!=j and i!=k and i!=m and j!=k and j!=m and k!=m and i!=n and j!=n and k!=n and m!=n and i!=o and j!=o and k!=o and m!=o and n!=o and i!=p and j!=p and k!=p and m!=p and n!=p and o!=p and i!=q and j!=q and k!=q and m!=q and n!=q and o!=q and p!=q and i!=r and j!=r and k!=r and m!=r and n!=r and o!=r and p!=r and q!=r and i!=s and j!=s and k!=s and m!=s and n!=s and o!=s and p!=s and q!=s and r!=s :
                                                    print(i,j,k,m,n,o,p,q,r,s)



#Team09
import os
import random

def play1():
    play2()


def play2():
    ans=[]
    t=0
    while t<4:
        num = str(random.randrange(10))
        if num not in ans:
            ans.append(num)
            t+=1

    #print (ans) #answer

    while True:
        print ("Guess a 4 digit number without repetition:")
        A=0
        B=0
        input1=input()


        try:
            int(input1)

            if "".join(str(n) for n in ans) == input1:
                print ("4,A,0,B")
                print ("Congratulation�� press anything to continue.\n")
                os.system('pause')
                play1()
            elif len(input1) != 4:
                print ("Error\n")

            else:
                for n in range(4):
                    if input1[n] == ans[n]:
                        A+=1
                    if input1[n] in ans:
                        B+=1

                print ("%d,A,%d,B" % (A, B-A))
        except:
            print ("Error\n")

play1()

#team 12
S2V = {'0': 0,
       '1': 1,
       '2': 2,
       '3': 3,
       '4': 4,
       '5': 5,
       '6': 6,
       '7': 7,
       '8': 8,
       '9': 9,
       'A': 10,
       'B': 11,
       'C': 12,
       'D': 13,
       'E': 14,
       'F': 15,
       'G': 16,
       'H': 17,
       'I': 18,
       'J': 19,
       'K': 20,
       'L': 21,
       'M': 22,
       'N': 23,
       'O': 24,
       'P': 25,
       'Q': 26,
       'R': 27,
       'S': 28,
       'T': 29,
       'U': 30,
       'V': 31,
       'W': 32,
       'X': 33,
       'Y': 34,
       'Z': 35,
       'a': 36,
       'b': 37,
       'c': 38,
       'd': 39,
       'e': 40,
       'f': 41,
       'g': 42,
       'h': 43,
       'i': 44,
       'j': 45,
       'k': 46,
       'l': 47,
       'm': 48,
       'n': 49,
       'o': 50,
       'p': 51,
       'q': 52,
       'r': 53,
       's': 54,
       't': 55,
       'u': 56,
       'v': 57,
       'w': 58,
       'x': 59,
       'y': 60,
       'z': 61}

def m2n():

    x = input("Please enter a number:")
    m = int(input("Please enter the initial base:"))
    n = int(input("Please enter the final base:"))

    integer = 0
    for character in x:
        assert character in S2V, "Unknown character!"
        value = S2V[character]
        assert value < m , "Digit outside base!"
        integer *= m
        integer += value

    V2S = dict(map(reversed, S2V.items()))

    array = []
    while integer !=0:
        value = integer % n
        integer //= n
        array.append(V2S[value])

    ans = "".join(reversed(array))

    print (ans)

m2n()
#team 14
>>> def lottery(n):
    import random
    k=0
    y=[]
    times=int(n)
    if k<times:
        number=random.int(1,49)
        y.append(number)
        k+=1
        return y
    else:
        print(y)


