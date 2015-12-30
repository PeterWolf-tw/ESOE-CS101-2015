#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#Team01
#設計一個程式
#若使用者輸入一個數值
#可算出該數值所具有的所有公因數
#例如輸入633
#可得1 3 211 633

def team01():
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



#Team02
'''''
def team02():
    lang=str(input ("give me a English word:"))
    #print (lang)
    x = len(lang)
    #print(x)
    lang2 = 'ay.'
    #print(lang2)
    lang1 = lang[1:x] + lang[0] + lang2
    print (lang1)
'''
def team02():
    Englishwords = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    lang=str(input ("give me a English word:"))
    #print (lang)
    x = len(lang)
    #print(x)
    lang2 = 'ay.'
    #print(lang2)

    for i in lang:
        if i in Englishwords:
            continue
        else:
            return False
    while (True):
        lang1 = lang[1:x] + lang[0] + lang2
        print (lang1)
        break



#Team04
#設計一個程式
#若input=n
#可算出費式數列第n項的值
#費式數列第n項的值等於第(n-1)項與第(n-2)項的和
#且a1=a2=1
def team04():
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


def team05():
    import math
    xdata=input("x=").split(",")
    xdata[:]=[int(a) for a in xdata]
    ydata=input("y=").split(",")
    ydata[:]=[int(b) for b in ydata]
    print(xdata)
    print(ydata)
    averagex=sum(xdata)/len(xdata)
    averagey=sum(ydata)/len(ydata)
    A=0
    B=0
    for a,b in zip (xdata,ydata):
        A+=(a-averagex)*(b-averagey)
        B+=(a-averagex)*(a-averagex)
    #print(A)
    #print(B)
    m=A/B
    print(m)
    k=averagey-m*averagex
    print(k)
    
    print("y=",end='')
    print(m,end='')
    print("x+",end='')
    print(k)
    
#Team06
#請輕鬆設計出一個可計算出任意個實數組之表準差的函數
# ex: input=(40,50,60) , output=8.164965809277....
# ex: input=(60,60,60,60) , output=0
def team06():
    LIST3 = []
    LIST4 = []
    LIST5 = []
    import math
    LIST3 = input("give me some numbers:").split(",")
    LIST3[:] = [float(a) for a in LIST3]
    #print (LIST3)
    average = sum(LIST3)/len(LIST3)
    #print (average)
    for n in range (0,len(LIST3),1):
        LIST4.append(LIST3[n] - average)
        LIST4[:] = [float(a) for a in LIST4]
    #print (LIST4)
    for n in range (0,len(LIST4),1):
        LIST5.append(math.pow(LIST4[n],2))
        LIST5[:] = [float(a) for a in LIST5]
    #print (LIST5)
    answer = math.sqrt(sum(LIST5) / len(LIST5))
    print (answer)    

#Team07
def team0701():
    n = int (input("give me a number:"))
    answer = 1
    for i in range (1, n+1,1):
        answer = answer*i
    return answer
    #print (answer)

def team0702():
    LIST = []
    LIST = input("Input some numbers:").split(' ')
    from itertools import permutations
    for i in permutations(LIST):
        print (i)


#Team09
def random():
    import random
    LIST = [0,1,2,3,4,5,6,7,8,9]
    ans = random.sample (LIST , 4)    
    return inputTest(ans)    
def inputTest(ans):
    
    #print(ans)
    y = []
    x=int(input("Try to guess a four digits number: "))
    y.append(x//1000)
    x=x-(1000*(x//1000))
    y.append(x//100)
    x=x-(100*(x//100))
    y.append(x//10)
    x=x-(10*(x//10))
    y.append(x//1)
    print(y)
    A=0
    B=0
    #print(ans[0])
    for a,b in zip(ans,y):
        if a==b:
            A+=1
    for a in y:
        if a in ans:
            B+=1
            
    #print(A)
    #print(B)

    B=B-A
     
    #print(A)
    #print(B)
    print(A,"A",B,"B")
    while A<4:
        return inputTest(ans)
    else:
        if input("Congratulation:), type q to quit, type anything to continue ") == "q":
            return None
        else :
            return random()




#Team10    
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




#Team12
def m2n():
    '''
    本函式將 m 進位制表示數轉為 n 進位制
    '''
    import math
    lang = input("輸入一串m進位的字串:")
    k = len(lang)
    element = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    a = input("m = ")
    elementa = element[0:int(a)]
    for i in lang:
        if i in elementa:
            continue
        else:
            return False
    while (True):
        #print (elementa)
        ten = 0
        ten +=int(elementa.index(lang[-1]))           
            
        #for i in range (0, len(lang)-1):
        for j in range(0,k-1):        
            l = elementa.index(lang[j])
            #print(int(l))
            x = k-1-int(j)
            #print (x)
            ten += int(l)*math.pow(int(a),x)
            #print (ten)
                
        print (ten)
            
        b = int(input("n = "))
        elementb = element[0:int(b)]
        c = int(ten)
        print(c//b)
        langans = []
        while c>0: 
            remider = c%b
            print (remider)
            langans.insert(0,elementb[remider])
            c = c//b
        answer = ''.join(langans)
        
        print(answer)
        break


#Team13
def team13():
    jon = ["Jon Snow",100,200,"t1",3]
    robert = ["Robert Stark",200,300,"t1",2]
    eddard = ["Eddard Stark",300,300,"t1",1]
    ser = ["Ser Rodrik",800,200,"t1",3]
    bran = ["Bran Stark",400,300,"t1",2]
    hodor = ["Hodor",900,400,"t1",3]
    rhaegar = ["Rhaegar Targargen",700,000,"t2",0]
    tywin = ["Tywin Lannister",500,500,"t3",2]
    jamie = ["Jamie Lannister",600,500,"t3",3]
    A=input("Who?")
    B=input("And who?")
    x = []
    x.append(A)
    y = []
    y.append(B)
    X =[]
    Y =[]
    #print(x)
    #print(y)
    for a,b,c,d,e,f,g,h,i in zip(jon,robert,eddard,ser,bran,hodor,rhaegar,tywin,jamie):
        if x[0]==jon[0]:
            X=jon
        if x[0]==robert[0]:
            X=robert
        if x[0]==eddard[0]:
            X=eddard    
        if x[0]==ser[0]:
            X=ser        
        if x[0]==rhaegar[0]:
            X=rhaegar        
        if x[0]==bran[0]:
            X=bran
        if x[0]==hodor[0]:
            X=hodor                            
        if x[0]==tywin[0]:
            X=tywin                            
        if x[0]==jamie[0]:
            X=jamie       
        if y[0]==jon[0]:
            Y=jon
        if y[0]==robert[0]:
            Y=robert
        if y[0]==eddard[0]:
            Y=eddard    
        if y[0]==ser[0]:
            Y=ser        
        if y[0]==rhaegar[0]:
            Y=rhaegar        
        if y[0]==bran[0]:
            Y=bran
        if y[0]==hodor[0]:
            Y=hodor                            
        if y[0]==tywin[0]:
            Y=tywin                            
        if y[0]==jamie[0]:
            Y=jamie
        if X==[] :
            print("You have the wrong name")
        if Y==[] :
            print("You have the wrong name")            
    #print(X)
    #print(Y)
    if X[1]==Y[1]:
        print("Stop Kidding Me! Asshole!!!")    
    elif X[1]==Y[2]:
        print(A,end=" ")
        print("是",end=" ")
        print(B,end=" ")
        print("的長官") 
    elif X[2]==Y[1]:
        print(A,end=" ")
        print("是",end=" ")
        print(B,end=" ")
        print("的屬下")       
    elif X[2]==Y[2]:
        print(A,end=" ")
        print("與",end=" ")
        print(B,end=" ")
        print("是平輩")
    elif X[3]!=Y[3]:
        print(A,end=" ")
        print("是",end=" ")
        print(B,end=" ")
        print("的敵人")
    elif X[3]==Y[3]:
        if X[4]==1:
            print(A,end=" ")
            print("是",end=" ")
            print(B,end=" ")
            print("的長官")
        elif Y[4]==1:
            print(A,end=" ")
            print("是",end=" ")
            print(B,end=" ")
            print("的屬下")             
        elif X[1]!=Y[2]:
            if X[2]!=Y[1]:
                print(A,end=" ")
                print("與",end=" ")
                print(B,end=" ")
                print("是平輩")         
    else:
        print("Stop Kidding Me! Asshole!!!")


#Team14
def team14(n):
    import random
    
    for i in range(0,n):    
        j=0
        resultLIST =[]
        while(j != 6):
            a = random.randint(1,49)
            if a not in resultLIST:
                resultLIST.append(a)
                j += 1
        resultLIST.sort()
        print(resultLIST)

    
if __name__== "__main__":
    print("team01:")
    t01 = team01()
    print(t01)
    
    print("team02:")
    print(team02())
    
    print("team04:")
    t04 = team04()
    print(t04)
    
    print("team05")
    t05 = team05()
    print(t05)
    
    print("team06:")
    t06 = team06()
    print(t06)
    
    print("team07")
    print (team0701())
    print (team0702())
    
    print("team09")
    print(random())
    
    print("team10:")
    t10 = team10()
    print(t10)
    
    print ("team12")
    print(m2n())    
    
    print("team13:")
    print(team13())
    
    print("team14:")
    print(team14(int(input("please give me a number:"))))
    
    
    
