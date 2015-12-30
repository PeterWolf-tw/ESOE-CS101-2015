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
    
#team08
def game():
    space = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    print ("|1|2|3|")
    print ("-------")
    print ("|4|5|6|")
    print ("-------")
    print ("|7|8|9|")
    n=1
    while True:
        
        if n%2 == 1 :
            a = int(input("playerX:"))
            if space[a-1] == "O" or space[a-1] == "X":
                continue
            space[a-1] = "X"
            print ("|%s|%s|%s|"%(space[0],space[1],space[2]))
            print ("-------")        
            print ("|%s|%s|%s|"%(space[3],space[4],space[5]))
            print ("-------")   
            print ("|%s|%s|%s|"%(space[6],space[7],space[8]))
            s1 = (space[0] == space[1] == space[2] == "X")
            s2 = (space[3] == space[4] == space[5] == "X")
            s3 = (space[6] == space[7] == space[8] == "X")
            s4 = (space[0] == space[3] == space[6] == "X")
            s5 = (space[1] == space[4] == space[7] == "X")
            s6 = (space[2] == space[5] == space[8] == "X")
            s7 = (space[0] == space[4] == space[8] == "X")
            s8 = (space[2] == space[4] == space[6] == "X")
            if s1 or s2 or s3 or s4 or s5 or s6 or s7 or s8 :
                print("playerX win")
                break
                print("playerO is fucked")
            if n == 9:
                print("DRAW")
                break
        if n%2 == 0 :
            a = int(input("playerO:"))
            if yee[a-1] == "O" or yee[a-1] == "X":
                continue            
            yee[a-1] = "O"
            print ("|%s|%s|%s|"%(space[0],space[1],space[2]))
            print ("-------")        
            print ("|%s|%s|%s|"%(space[3],space[4],space[5]))
            print ("-------")   
            print ("|%s|%s|%s|"%(space[6],space[7],space[8]))
            s1 = (space[0] == space[1] == space[2] == "O")
            s2 = (space[3] == space[4] == space[5] == "O")
            s3 = (space[6] == space[7] == space[8] == "O")
            s4 = (space[0] == space[3] == space[6] == "O")
            s5 = (space[1] == space[4] == space[7] == "O")
            s6 = (space[2] == space[5] == space[8] == "O")
            s7 = (space[0] == space[4] == space[8] == "O")
            s8 = (space[2] == space[4] == space[6] == "O")
            if s1 or s2 or s3 or s4 or s5 or s6 or s7 or s8 :
                print("playerX is fucked")
                break
            if n == 9:
                print("DRAW")
                break
        n += 1

#team09
def yayaya():
    a = 0
    import random
    num = []
    while(len(num)<4):
        r = random.randint(0, 9)
        r = str(r)
        if r not in num :
            num.append(r)    
    while(a < 4):
        inputSTR = input("--->")
        gg = list(inputSTR)
        a=0
        b=0
        import random
        
        for i in range(0,4):
            if gg[i] == num[i] :
                a += 1
            else :
                if gg[i] in num :
                    b += 1
        print(a, end ='')
        print("A", end ='')
        print(b, end ='')
        print("B")
    return ''
    
#Team10
def jable():
    for i in range(0,10):
        for j in range(0,10):
            if i*j < 10:
                print(i*j,end='')
                print("  ",end='')
            else:
                print(i*j,end='')
                print(" ",end='')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    return "Table of Js"
if __name__ == '__main__':
    print(jable())

#team14
import random 

def gamble(x):
    gg=list(range(1,50)) 
    n = []
    y = int(x)
    while y>0:
        n.append(random.sample(gg,6))
        y -= 1
    return n  
  

x = input('please insert a number: ')
print(gamble(x))
