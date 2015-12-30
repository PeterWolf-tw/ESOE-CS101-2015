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

#Team02#######################
def team02(a):
    result = ''
    b = list(a)
    b.append(b[0])
    b.append('ay')
    b.remove(b[0])
    for i in b :
        result = result + i
    
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

#Team06########################
def team06():
    import math
    fuck = []
    a=0
    th=0
    while (a==0):
        fuck.append(float(input("輸入數字>>>")))
        a = int(input("owari? (hai=1 , iie=0):"))
    mu = sum(fuck)/len(fuck)
    for i in fuck:
        th = th+ (i-mu)**2
    result = th/len(fuck)
    result = math.sqrt(result)
    return result

#Team08#########################
def team08():
    yee = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    print ("1|2|3")
    print ("-----")
    print ("4|5|6")
    print ("-----")
    print ("7|8|9")
    n=1
    while True:
        
        if n%2 == 1 :
            a = int(input("X輸入:"))
            if yee[a-1] == "O" or yee[a-1] == "X":
                print("8787")
                continue
            yee[a-1] = "X"
            print ("%s|%s|%s"%(yee[0],yee[1],yee[2]))
            print ("-----")        
            print ("%s|%s|%s"%(yee[3],yee[4],yee[5]))
            print ("-----")   
            print ("%s|%s|%s"%(yee[6],yee[7],yee[8]))
            s1 = (yee[0] == yee[1] == yee[2] == "X")
            s2 = (yee[3] == yee[4] == yee[5] == "X")
            s3 = (yee[6] == yee[7] == yee[8] == "X")
            s4 = (yee[0] == yee[3] == yee[6] == "X")
            s5 = (yee[1] == yee[4] == yee[7] == "X")
            s6 = (yee[2] == yee[5] == yee[8] == "X")
            s7 = (yee[0] == yee[4] == yee[8] == "X")
            s8 = (yee[2] == yee[4] == yee[6] == "X")
            if s1 or s2 or s3 or s4 or s5 or s6 or s7 or s8 :
                print("X贏了")
                break
            
            if n == 9:
                print("平手")
                break
        if n%2 == 0 :
            a = int(input("O輸入:"))
            if yee[a-1] == "O" or yee[a-1] == "X":
                print("8787")
                continue            
            yee[a-1] = "O"
            print ("%s|%s|%s"%(yee[0],yee[1],yee[2]))
            print ("-----")        
            print ("%s|%s|%s"%(yee[3],yee[4],yee[5]))
            print ("-----")   
            print ("%s|%s|%s"%(yee[6],yee[7],yee[8]))
            s1 = (yee[0] == yee[1] == yee[2] == "O")
            s2 = (yee[3] == yee[4] == yee[5] == "O")
            s3 = (yee[6] == yee[7] == yee[8] == "O")
            s4 = (yee[0] == yee[3] == yee[6] == "O")
            s5 = (yee[1] == yee[4] == yee[7] == "O")
            s6 = (yee[2] == yee[5] == yee[8] == "O")
            s7 = (yee[0] == yee[4] == yee[8] == "O")
            s8 = (yee[2] == yee[4] == yee[6] == "O")
            if s1 or s2 or s3 or s4 or s5 or s6 or s7 or s8 :
                print("O贏了")
                break
            if n == 9:
                print("平手")
                break
        n += 1

#Team09#######################
def team09():
    a = 0
    import random
    yee = []
    while(len(yee)<4):
        rand = random.randint(0, 9)
        rand = str(rand)
        if rand not in yee :
            yee.append(rand)    
    while(a < 4):
        inputSTR = input(">>>")
        fuck = list(inputSTR)
        a=0
        b=0
        import random
        
        #print(yee)
        for i in range(0,4):
            if fuck[i] == yee[i] :
                a += 1
            else :
                if fuck[i] in yee :
                    b += 1
        print(a, end ='')
        print("A", end ='')
        print(b, end ='')
        print("B")
    return ''

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
#Team11##################################
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
        
if __name__== "__main__":
    print("team01:")
    t01 = int(input('>>>'))
    print(asiagodtone(t01))
    
    print("team02:")
    t02 = input('>>>')
    print(team02(t02))    
    
    print("team04:")
    t04 = int(input('>>>'))
    print(fibonacci(t04))
    
    print("team06:")
    t06 = (team06())
    print(t06)
    
    print("team08:")
    print(team08())
    
    print('team09:')
    print(team09())
    
    print("team10:")
    t10 = team10()
    print(t10)
    
    print("Team11:")
    t11 = int(input("玩家人數:"))
    print(team11(t11))    
    
    print("Team12:")
    t12 = input("輸入數字>>>")
    t12a = int(input("進位法1>>>"))
    t12b = int(input("進位法2>>>"))
    print(translater(t12))
    print(ntom(t12,t12a,t12b))    
    
    print("team14:")
    t14 = lottery(int(input("輸入:")))
    print(t14)
    