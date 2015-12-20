#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#Team01###############
def asiagodtone(yee):
    result = []
    

    for i in range(1,yee+1):
        if yee%i == 0 :
            result.append(i)
            

            
        else:
            continue
    return result

#Team04#####################
def fibonacci(yee):
    fibo = []
    for i in range(0,yee):
        if i == 0 or i == 1 :
            fibo.append(1)
        else:
            fibo.append(fibo[i-1]+fibo[i-2])
    
    return fibo

#Team10#######################
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

#Team12##################################
def index():
    fuck = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    shit = []
    j = 0
    for i in fuck:
        shit.append((i,j))
        j = j+1
    return shit

def translater(inputSTR):
    yee = index()
    out = []
    for i in inputSTR:
        for j in yee:
            if i in j :
                out.append(j[1])

            else :
                continue
    return out          

def ntom(inputSTR,a,b):
    
    anum = translater(inputSTR)
    #a = 16
    #b = 2
    bnum = []
    s = 0
    j = len(anum)
    result = ""
    for i in anum:
        s = s + i*(a**(j-1))
        j = j-1
    while(s != 0):
        bnum.append(s%b)
        s = s - s%b
        s = s//b
    bnum.reverse()
    for i in bnum:
        for j in index():
            if i in j :
                result = result + j[0]
    
    return result

#Team14########################
def lottery():
    import random
    fuck = []
    result = []
    for i in range(0,49):
        fuck.append(i)
    
    for i in range(0,6):
        srand = random.randint(0,48-i)
        result.append(fuck[srand])
        del fuck[srand]
    result.sort()
    return result
        
if __name__== "__main__":
    print("team01:")
    t01 = int(input('>>>'))
    print(asiagodtone(t01))
    
    print("team04:")
    t04 = int(input('>>>'))
    print(fibonacci(t04))
    
    print("team10:")
    t10 = team10()
    print(t10)
    
    print("Team12:")
    t12 = input("輸入數字>>>")
    t12a = int(input("進位法1>>>"))
    t12b = int(input("進位法2>>>"))
    print(translater(t12))
    print(ntom(t12,t12a,t12b))    
    
    print("team14:")
    t14 = lottery()
    print(t14)