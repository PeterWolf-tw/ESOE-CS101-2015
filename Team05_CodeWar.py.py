#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#第一組 求因數

def commondivisor(inputnumber):
    resultList = []
    numberlist = ["1","2","3","4","5","6","7","8","9","0"]
    a = int(inputnumber)
    b = 1
    
    d = str(inputnumber)
    e = list(d)
    for i in e:
        if i in numberlist:
            pass
        else:
            h = "false! A positive integer!"
            return h
    while a >= b:
        c = (a % b) 
        if c == 0:
            resultList.append(b)
            resultList.append(-b)
        b += 1
        f = list(set(resultList))
        g = sorted(f)        
        
    return g

if __name__ == "__main__":
    r = ("please input a positive integer： ")
    k = input(r)
    k = int(k)
    i = commondivisor(k)
    print(i)
    

    
#第二組 piglatin遊戲

def piglatin(inputword):
    letterList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    a = str(inputword) 
    b = list(a)

    for i in b:
        if i in letterList:
            pass
        else:
            d = "false!! Please input a goddamn ENGLISH word!!"
            return d
    c = b.pop(0)
    b.append(c)
    b.append("ay")
    e = ''.join(b)
    return e


if __name__ == "__main__": 
    x = ("please input a ENGLISH word： ")
    y = input(x)  
    r = piglatin(y)
    print(r)
    

#第三組 class


#第四組 費氏數列

#一般版
def fn(a):
    fnlist = [1,1]
    for i in range(a+2):
        fnlist[i+2:]=[0]        
        fnlist[i+2] = fnlist[i+1]+fnlist[i+0]
    print (fnlist[a-1])
if __name__ == "__main__":
    fn(5)
    #test area

#公式版    
def fnm(a):
    b = (5**-0.5)*(((1+5**0.5)/2)**a-((1-5**0.5)/2)**a)
    b=b//1
    print(b)
if __name__ == "__main__":
    fnm(20)
    

#第五組 我們自己(最小方差)


#第六組 標準差

def sd(a):
    import math as math
    a2 = 0
    for i in range(len(a)):
        a2 = a2 + a[i]**2
    a3 = 0
    for k in range(len(a)):
        a3 = a3 + a[k]
    a4 = a2/len(a) - (a3/len(a))**2
    ans = math.sqrt(a4)
    print(ans)
if __name__ == "__main__":
    sd([40,50,60])
    
    
#第七組 排列組合

import itertools


def factorial(n):
    
    a = int(n)
    for i in range(a):          # 階層的和
        factorial = 1
        for j in range(i+1):          # 階層
            factorial *= (j+1)  
    return factorial

def permutation(x,y):
    a = list(x)
    b = y
    r = len(x)
    if b > r:
        z = "你在亂打什麼？"
        return z
    else:
        pass
    c = list(itertools.permutations(a,b))
    g = ""
    for i in c:
        #d = print(i)
        g = g + ' '.join(i) + "\n"
    return g
    
    
if __name__ == "__main__":
    a = input("請輸入一個正整數n： ")
    b = int(a)
    c = factorial(b)
    d = input("請輸入n個正整數： ")
    e = permutation(d,b)
    print(c)
    print(e)




#第八組 圈圈叉叉


sit = [" "," "," "," "," "," "," "," "," "]
def maincode(name1list,name2list,name1,name2):
    sit = [" "," "," "," "," "," "," "," "," "]
    print("\\","x","0"," "," "," ","1"," "," "," ","2"," ")
    print("y","\\"," "," ","|"," "," "," ","|"," "," "," ")
    print("0"," ",sit[0]," ","|"," ",sit[1]," ","|"," ",sit[2]," ")
    print(" "," "," "," ","|"," "," "," ","|"," "," "," ")
    print(" ","-","-","-","-","-","-","-","-","-","-","-")
    print(" "," "," "," ","|"," "," "," ","|"," "," "," ")
    print("1"," ",sit[3]," ","|"," ",sit[4]," ","|"," ",sit[5]," ")
    print(" "," "," "," ","|"," "," "," ","|"," "," "," ")
    print(" ","-","-","-","-","-","-","-","-","-","-","-")
    print(" "," "," "," ","|"," "," "," ","|"," "," "," ")
    print("2"," ",sit[6]," ","|"," ",sit[7]," ","|"," ",sit[8]," ")
    print(" "," "," "," ","|"," "," "," ","|"," "," "," ")
    print()
    i=1
    i=1
    dictionary = {"0-0":0,"0-1":1,"0-2":2,"1-0":3,"1-1":4,"1-2":5,"2-0":6,"2-1":7,"2-2":8}
    proper=["0-0","0-1","0-2","1-0","1-1","1-2","2-0","2-1","2-2"]
    bingo=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]    
    while i==1:
        print("\\","x","0"," "," "," ","1"," "," "," ","2"," ")
        print("y","\\"," "," ","|"," "," "," ","|"," "," "," ")
        print("0"," ",sit[0]," ","|"," ",sit[1]," ","|"," ",sit[2]," ")
        print(" "," "," "," ","|"," "," "," ","|"," "," "," ")
        print(" ","-","-","-","-","-","-","-","-","-","-","-")
        print(" "," "," "," ","|"," "," "," ","|"," "," "," ")
        print("1"," ",sit[3]," ","|"," ",sit[4]," ","|"," ",sit[5]," ")
        print(" "," "," "," ","|"," "," "," ","|"," "," "," ")
        print(" ","-","-","-","-","-","-","-","-","-","-","-")
        print(" "," "," "," ","|"," "," "," ","|"," "," "," ")
        print("2"," ",sit[6]," ","|"," ",sit[7]," ","|"," ",sit[8]," ")
        print(" "," "," "," ","|"," "," "," ","|"," "," "," ")    
        print("Please Enter The Place IN THE FORM OF y-x, such as 1-1 or 2-1")
        z=1
        while z==1:
            one = input("What do you want to place the O, "+name1+"?")
            if one in proper:
                z=2
            else:
                pass
        k=dictionary[one]
        sit[k] = "O"
        name1list.append(k)
        for l in name1list:
            if l in name2list:
                exit("what are you doing?")
                i=2
                quit
            else:
                pass
        for j in bingo:
            if (j[0] in name1list) and (j[1] in name1list) and (j[2] in name1list):
                print(name1,"bingo")
                i=2
                quit(maincode)
                return i
            else:
                pass
        print("\\","x","0"," "," "," ","1"," "," "," ","2"," ")
        print("y","\\"," "," ","|"," "," "," ","|"," "," "," ")
        print("0"," ",sit[0]," ","|"," ",sit[1]," ","|"," ",sit[2]," ")
        print(" "," "," "," ","|"," "," "," ","|"," "," "," ")
        print(" ","-","-","-","-","-","-","-","-","-","-","-")
        print(" "," "," "," ","|"," "," "," ","|"," "," "," ")
        print("1"," ",sit[3]," ","|"," ",sit[4]," ","|"," ",sit[5]," ")
        print(" "," "," "," ","|"," "," "," ","|"," "," "," ")
        print(" ","-","-","-","-","-","-","-","-","-","-","-")
        print(" "," "," "," ","|"," "," "," ","|"," "," "," ")
        print("2"," ",sit[6]," ","|"," ",sit[7]," ","|"," ",sit[8]," ")
        print(" "," "," "," ","|"," "," "," ","|"," "," "," ")
        print()
        print("Please Enter The Place IN THE FORM OF y-x, such as 1-1 or 2-1")
        f=1
        while f==1:
            two = input("What do you want to place the X, "+name2+"?")
            if two in proper:
                f=2
            else:
                pass
        h=dictionary[two]
        sit[h] = "X"
        name2list.append(h)
        for d in name2list:
            if d in name1list:
                exit("what are you doing?")
                i=2
                break
            else:
                pass
        for k in bingo:
            if (k[0] in name2list) and (k[1] in name2list) and (k[2] in name2list):
                print(name2,"bingo")
                i=2
                quit(maincode)
                return i
            else:
                pass        
def tic_tac_toe(sit):
    import sys
    print("\\","x","0"," "," "," ","1"," "," "," ","2"," ")
    print("y","\\"," "," ","|"," "," "," ","|"," "," "," ")
    print("0"," ",sit[0]," ","|"," ",sit[1]," ","|"," ",sit[2]," ")
    print(" "," "," "," ","|"," "," "," ","|"," "," "," ")
    print(" ","-","-","-","-","-","-","-","-","-","-","-")
    print(" "," "," "," ","|"," "," "," ","|"," "," "," ")
    print("1"," ",sit[3]," ","|"," ",sit[4]," ","|"," ",sit[5]," ")
    print(" "," "," "," ","|"," "," "," ","|"," "," "," ")
    print(" ","-","-","-","-","-","-","-","-","-","-","-")
    print(" "," "," "," ","|"," "," "," ","|"," "," "," ")
    print("2"," ",sit[6]," ","|"," ",sit[7]," ","|"," ",sit[8]," ")
    print(" "," "," "," ","|"," "," "," ","|"," "," "," ")
    i=1
    dictionary = {"0-0":0,"0-1":1,"0-2":2,"1-0":3,"1-1":4,"1-2":5,"2-0":6,"2-1":7,"2-2":8}
    proper=["0-0","0-1","0-2","1-0","1-1","1-2","2-0","2-1","2-2"]
    bingo=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    d=1
    while d==1:
        name1list = []
        name2list = []
        name1 = input("Waht is the O name?")
        name2 = input("Waht is the X name?")            
        maincode(name1list,name2list,name1,name2)
        quit(tic_tac_toe)
    if i==2:
        c = input("Do you want to game?y/n")
        if c=="y":
            i=1
            name1list = []
            name2list = []
            name1 = input("Waht is the O name?")
            name2 = input("Waht is the X name?")                
            maincode(name1list,name2list,name1,name2)
        else:
            exit
if __name__ == "__main__":
    import sys
    tic_tac_toe(sit)
  
    
    
#第九組 幾A幾B


import random
import os
ST=[]
t=0
while t<4 :
    tem=str(random.randrange(0,9))
    if not (tem in ST):
        ST.append(tem)
        t+=1
#宣告一個ST,存放亂數產生要猜的一組不重覆的四位數{
time=1
while True:
    print (u"猜第%d次。\n請輸入一個不重覆的四位數字或輸入'STOP'以退出遊戲:" %time)
    A=0
    B=0
    input_s=input()
    if "STOP" in input_s.upper():
        print (u"離開遊戲! 正確答案為 %s" % "".join(str(n) for n in ST))
        break
    else:
        try:
            int(input_s)    #測試是否輸入的為數字,若非會產生列外處理
            if "".join(str(n) for n in ST)==input_s: #猜到數字,結束遊戲
                print (u"Good Job!! 共猜了 %d 次" %time)
                break
            elif len(input_s) != 4:
                print (u"錯誤! 不正確的長度!\n")
            else:   #未猜到,計算與目標數字的差異
                for tem in range(4):
                    if ST[tem] == input_s[tem]: #包括、且位置相符
                        A+=1
                    if input_s[tem] in ST:  #計算包括的數字,所以需再減去A的總合,才是僅包括,但位置不同的數量
                        B+=1
                print ("%d A\t%d B" % (A,B-A))
                time+=1
        except:
            print (u"錯誤! 內含非數字的字串\n")
os.system("pause")



#第十組 99乘法表

def multiply(x,y):
    a = (x+1)*(y+1)
    board = ["0" for i in range((x+1)*(y+1))]
    i = 0
    for j in range(x+1):
        for k in range(y+1):
            a = str(j) + "x" + str(k) + "=" + str(j*k) + " "        
            if len(str(x+1) + "x" + str(k) + "=" + str((x+1)*k) + " ") > len(str(j) + "x" + str(k) + "=" + str(j*k) + " "):
                b = len(str(x+1) + "x" + str(k) + "=" + str((x+1)*k) + " ") - len(str(j) + "x" + str(k) + "=" + str(j*k) + " ")
                for l in range(b):
                    a = " " + a
            board[i] = a
            i += 1
            
    print ('\n'.join(''.join(board[i:i+(x+1)]) for i in range(0,(x+1)*(y+1),(x+1))))    


if __name__== "__main__":
    x = 9
    y = 9
    result = multiply(x,y)
    print(result)
    
    
#第十一組 猜數字遊戲

def GuessNumber():
    import random                                         
    howmany = input("多少人(參賽者2~5人)?")
    howmany = numbercheck(howmany)
    nameLIST = []
    fncardDICT = {}
    for i in range(0,howmany):
        cname = namecheck(i,nameLIST)
        nameLIST.append(cname)
        fncardDICT[nameLIST[i]] = 1     
    undercover = nameLIST[random.randint(0,howmany-1)]
    fncardDICT[undercover] = 0
    bomb = random.randint(1, 36)
    s = 0
    o = 1
    return playing(o,s,nameLIST[0],nameLIST,fncardDICT,undercover,bomb,howmany)


def numbercheck(howmany):                                   #判斷玩家人數輸入正確
    try:
        if int(howmany) in range(2,6):
            return int(howmany)
        else:
            print("人數錯誤!")
            return GuessNumber()            
    except ValueError:
        print ("請輸入整數")
        return GuessNumber()
    
        
def namecheck(i,nameLIST):                                  #判斷名字不能重複
        print("玩家",i+1,"你的名字是?")
        name = input()
        if name in nameLIST:
            print ("這個名字已經被取過了")
            return namecheck(i,nameLIST)
        else:
            return name
        

def playing(o,s,who,nameLIST,fncardDICT,undercover,bomb,howmany):              #輪流輸入
    print("")
    print("現在數字加到",s,"！")
    if who == undercover:
        print("玩家",who,"你知道答案是:",bomb)        
    if fncardDICT[who] == 1:
        print("玩家",who,",你可輸入數字1~3 or pass or return")
    if fncardDICT[who] == 0:
        print("玩家",who,",你可輸入數字1~3")    
    reply = input()
    if reply == "return" and fncardDICT[who] >= 1:
        fncardDICT[who] = 0
        o *= -1
        who = nameLIST[(nameLIST.index(who) + o) % howmany]
        return playing(o,s,who,nameLIST,fncardDICT,undercover,bomb,howmany)
    if reply == "pass" and fncardDICT[who] >= 1:
        fncardDICT[who] = 0
        who = nameLIST[(nameLIST.index(who) + o) % howmany]
        return playing(o,s,who,nameLIST,fncardDICT,undercover,bomb,howmany)
    if reply == "1" or reply == "2" or reply == "3":
        s += int(reply)
        if s >= bomb:
            print("答案是",bomb)
            print(who,"輸了")
            print("遊戲結束")    
            input("按Enter鍵開始下一輪遊戲")
            print("")
            return GuessNumber()                         
        who = nameLIST[(nameLIST.index(who) + o) % howmany]
        return playing(o,s,who,nameLIST,fncardDICT,undercover,bomb,howmany)             
    else:
        print("輸入錯誤,請重新輸入")
        print("")
        return playing(o,s,who,nameLIST,fncardDICT,undercover,bomb,howmany)              
    

if __name__ == "__main__":

    result = GuessNumber()
    print(result)


#第十二組 進位轉換

def m2n():
    '''
    本函式將 m 進位制表示數轉為 n 進位制
    '''    
    iSTR = input("輸入要轉換的字串:")
    a = input("原進位數m = ")
    b = input("欲轉換進位數n = ")
    nSTR = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    try:
        if "." in a or "." in b or int(a) not in range(2,62) or int(b) not in range(2,62):
            return "請輸入2~61之間的正整數"
    except ValueError:
        return "請輸入2~61之間的正整數"
    for i in range(int(a),len(nSTR)):
        if nSTR[i] in iSTR:
            return "要計算的字串與輸入的進位數不合"
    s = 0
    for i in range(len(iSTR)-1,-1,-1):
       for j in range(len(nSTR)):
            if iSTR[i] == nSTR[j]:
                s += j * (int(a) ** (len(iSTR)-i-1))  
    c = ""
    (d, m) = divmod(s, int(b))
    while d > 0:
        c = str(nSTR[m]) + c
        (d, m) = divmod(d, int(b))
    c = str(nSTR[m]) + c
    return c

if __name__ == "__main__":
    print(m2n())
    

#第十三組 權力遊戲


def GAMEOFTHRONES(a,b):
    characterlist = [("Jon Snow"),("Robert Stark"),("Eddard Stark"),("Bran Stark"),("Tywin Lannister"),("Jamie Lannister"),("Ser Rodrik"),("Hodor"),("Rhaegar Targaryen")]
    z = characterlist
    resultlist1 = [("jon snow"),("robert stark")]
    resultlist2 = [("jon snow"),("eddard stark")]
    resultlist3 = [("jon snow"),("bran stark")]
    resultlist4 = [("jon snow"),("tywin lannister")]
    resultlist5 = [("jon snow"),("jamie lannister")]
    resultlist6 = [("jon snow"),("ser rodrik")]
    resultlist7 = [("jon snow"),("hodor")]
    resultlist8 = [("jon snow"),("rhaegar targaryen")]
    resultlist9 = [("robert stark"),("eddard stark")]
    resultlist10 = [("robert stark"),("bran stark")]
    resultlist11 = [("robert stark"),("tywin lannister")]
    resultlist12 = [("robert stark"),("jamie lannister")]
    resultlist13 = [("robert stark"),("ser rodrik")]
    resultlist14 = [("robert stark"),("hodor")]
    resultlist15 = [("robert stark"),("rhaegar targaryen")]
    resultlist16 = [("eddard stark"),("bran stark")]
    resultlist17 = [("eddard stark"),("tywin lannister")]
    resultlist18 = [("eddard stark"),("jamie lannister")]
    resultlist19 = [("eddard stark"),("ser rodrik")]
    resultlist20 = [("eddard stark"),("hodor")]
    resultlist21 = [("eddard stark"),("rhaegar targaryen")]
    resultlist22 = [("bran stark"),("tywin lannister")]
    resultlist23 = [("bran stark"),("jamie lannister")]
    resultlist24 = [("bran stark"),("ser rodrik")]
    resultlist25 = [("bran stark"),("hodor")]
    resultlist26 = [("bran stark"),("rhaegar targaryen")]
    resultlist27 = [("tywin lannister"),("jamie lannister")]
    resultlist28 = [("tywin lannister"),("ser rodrik")]
    resultlist29 = [("tywin lannister"),("hodor")]
    resultlist30 = [("tywin lannister"),("rhaegar targaryen")]
    resultlist31 = [("jamie lannister"),("ser rodrik")]
    resultlist32 = [("jamie lannister"),("hodor")]
    resultlist33 = [("jamie lannister"),("rhaegar targaryen")]
    resultlist34 = [("ser rodrik"),("hodor")]
    resultlist35 = [("ser rodrik"),("rhaegar targaryen")]
    resultlist36 = [("hodor"),("rhaegar targaryen")]
    if a in resultlist1:
        if b in resultlist1:
            print("Robert Stark是Jon Snow的長官!")

    
    if a in resultlist2:
        if b in resultlist2:
            print("Eddard Stark是Jon Snow的長官的長官!")   

    if a in resultlist3:
        if b in resultlist3:
            print("Bran Stark和Jon Snow為平輩!")
                
    if a in resultlist4:
        if b in resultlist4:
            print("Jon Snow和Tywin Lannister為敵人!")
            
    if a in resultlist5:
        if b in resultlist5:
            print("Jon Snow和Jamie Lannister為敵人!")
            
    if a in resultlist6:
        if b in resultlist6:
            print("Jon Snow和Ser Rodrik為平輩!")   
            
    if a in resultlist7:
        if b in resultlist7:
            print("Hodor和Jon Snow為平輩!")   
            
    if a in resultlist8:
        if b in resultlist8:
            print("資料有誤無法比對!")   
            
    if a in resultlist9:
        if b in resultlist9:
            print("Robert Stark為Eddard Stark的屬下!")    
            

    if a in resultlist10:
        if b in resultlist10:
            print("Bran Stark和Robert Stark為平輩!")            
            
    if a in resultlist11:
        if b in resultlist11:
            print("Robert Stark是Tywin Lannister的敵人!")  
            
    if a in resultlist12:
        if b in resultlist12:
            print("Robert Stark是Jamie Lannister的敵人!")
            
                        
    if a in resultlist13:
        if b in resultlist13:
            print("Robert Stark是Ser Rodrik的老大!") 
            
    if a in resultlist14:
        if b in resultlist14:
            print("Hodor是Robert Stark的長官的屬下的屬下!")
            
    if a in resultlist15:
        if b in resultlist15:
            print("資料有誤無法比對!")  
            
    if a in resultlist16:
        if b in resultlist16:
            print("Eddard Stark是Bran Stark的長官!")     
            
    if a in resultlist17:
        if b in resultlist17:
            print("Eddard Stark是Tywin Lannister的敵人!")
            
    if a in resultlist18:
        if b in resultlist18:
            print("Eddard Stark是Jamie Lannister的敵人!")
            
    if a in resultlist19:
        if b in resultlist19:
            print("Eddard Stark是Ser Rodrik的長官的長官!") 
            
    if a in resultlist20:
        if b in resultlist20:
            print("Eddard Stark是Hodor的長官的長官!")
            
    if a in resultlist21:
        if b in resultlist21:
            print("資料有誤無法比對!")  
            
    if a in resultlist22:
        if b in resultlist22:
            print("Bran Stark是Tywin Lannister的敵人!") 
            
    if a in resultlist23:
        if b in resultlist23:
            print("Bran Stark和Jamie Lannister是敵人!") 
            
    if a in resultlist24:
        if b in resultlist24:
            print("Bran Stark和Ser Rodrik為平輩!") 
            
    if a in resultlist25:
        if b in resultlist25:
            print("Bran Stark是Hodor的長官!")
            
    if a in resultlist26:
        if b in resultlist26:
            print("資料有誤無法比對!") 
            
    if a in resultlist27:
        if b in resultlist27:
            print("Tywin Lannister是Jamie Lannister的長官!")
            
    if a in resultlist28:
        if b in resultlist28:
            print("Tywin Lannister和Ser Rodrik鬥爭!")     
    
    if a in resultlist29:
        if b in resultlist29:
            print("Tywin Lannister和Hodor打架!")

    if a in resultlist30:
        if b in resultlist30:
            print("資料有誤無法比對!")   
            
    if a in resultlist31:
        if b in resultlist31:
            print("Jamie Lannister是Ser Rodrik的敵人!")
            
    if a in resultlist32:
        if b in resultlist32:
            print("Jamie Lannister和Hodor開戰!")     
            
    if a in resultlist33:
        if b in resultlist33:
            print("資料有誤無法比對!") 

    if a in resultlist34:
        if b in resultlist34:
            print("Ser Rodrik是Hodor的長官的長官的屬下的屬下!")
            
    if a in resultlist35:
        if b in resultlist35:
            print("兩人關係無解!") 
                        
    if a in resultlist36:
        if b in resultlist36:
            print("資料有誤無法比對!")     
if __name__ == "__main__":
    print("權力遊戲主要角色：Jon Snow,Robert Stark,Eddard Stark,Bran Stark,Tywin Lannister,Jamie Lannister,Ser Rodrik,Hodor,Rhaegar Targaryen")
    
    a = ("請輸入一個權力遊戲的人名： ")
    b = ("請輸入另一個： ")

    c = input(a)
    d = input(b)
    x = str.lower(c)
    y = str.lower(d)    
    e = GAMEOFTHRONES(x,y)
    print(e)
    
    
    
#第十四組 隨機樂透

def ran(n):
    import random
    i=0
    while i<n:
        a = random.sample(range(1, 50), 6)
        print(a)
        i = i + 1 
if __name__ == "__main__":
    ran(6)

