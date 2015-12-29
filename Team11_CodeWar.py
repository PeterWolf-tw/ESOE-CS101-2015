#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#第一組
def team1():
    n = int(input("which number?"))
    k = []
    for i in range(n):
        if int(n/(i+1)) == n/(i+1):
            k.append(i+1)
            k.append(-i-1)
    print (k)

#第二組
def team2():
    word = input("enter a word in English:")
    if str.isalpha(word) != True:
        print("87??")
    else:
        first = word[0]
        word = word[1:] + first + "ay."
        print (word)
        
#第三組
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

#第四組
def team4():
    n = int(input("要第幾個數?"))
    if n < 1:
        print("87?")
    l = [0,1,1]
    for i in range(n+1):
        if i > 2:
            l.append(l[i-2]+l[i-1])
    if n >= 0:
        print(l[n])

#第五組
def team5(a,b):

    aveX = sum(a)/len(a)
    aveY = sum(b)/len(b)
    SDX0 = 0
    for i in a:
        SDX0 = SDX0 + (i - aveX)**2
    SDY0 = 0
    for j in b:
        SDY0 = SDY0 + (j - aveY)**2
    r0 = 0
    for k in range(len(a)):
        r0 = r0 + (a[k]-aveX)*(b[k]-aveY)
    r = r0/(SDX0)
    
    h = (-(aveX)*r + aveY)
    print(r)
    print("y = ",round(r,4),"x + ",round(h,5))

#第六組
def team6():
    numberlist = []
    m = int(input("how many number do you want to analyze?"))
    for i in range(m):
        n = float(input("第%s個數?"%(i+1)))
        numberlist.append(n)
    average = sum(numberlist) / len(numberlist)
    re1 = 0
    for i in numberlist:
        re1 += (i - average)**2
    re2 = (re1/len(numberlist))**0.5
    print(re2)
    
#第七組    
    from itertools import permutations
    
    def team7() :
        n = int(input("要輸入幾個數字呢?"))
        yee = [] 
        np = 1
        for i in range(n):
            k = int(input("第%s個數為?"%(i+1)))
            yee.append(k)
            np = (i+1)*np
        print (np)
        print (list(permutations(yee,n)))        

#第八組
    def team8():
        l=[" "," "," "," "," "," "," "," "," "]
        print("introduction:please enter 1~9 to mark corresponding square")
        print("1|2|3")
        print ("-----")
        print ("4|5|6")
        print ("-----")
        print ("7|8|9")
        while True:
            while True:
                n = int(input("P1's turn:"))
                if 10 > n > 0 and l[n-1]==" ":
                    l[n-1] = "O"
                    print ("%s|%s|%s"%(l[0],l[1],l[2]))
                    print ("-----")        
                    print ("%s|%s|%s"%(l[3],l[4],l[5]))
                    print ("-----")   
                    print ("%s|%s|%s"%(l[6],l[7],l[8]))
    
                    break
                else : 
                    print("wrong instruction,try again")
                    continue
            s1 = (l[0] == l[1] == l[2] == "O")
            s2 = (l[3] == l[4] == l[5] == "O")
            s3 = (l[6] == l[7] == l[8] == "O")
            s4 = (l[0] == l[3] == l[6] == "O")
            s5 = (l[1] == l[4] == l[7] == "O")
            s6 = (l[2] == l[5] == l[8] == "O")
            s7 = (l[0] == l[4] == l[7] == "O")
            s8 = (l[2] == l[4] == l[6] == "O")        
            if s1 or s2 or s3 or s4 or s5 or s6 or s7 or s8:
                print("P1 win!")
                break
            if " " not in set(l):
                print("平手")
                break
            
            while True:
                n = int(input("P2's turn:"))
                if 10 > n > 0 and l[n-1]==" ":
                    l[n-1] = "X"
                    print ("%s|%s|%s"%(l[0],l[1],l[2]))
                    print ("-----")        
                    print ("%s|%s|%s"%(l[3],l[4],l[5]))
                    print ("-----")   
                    print ("%s|%s|%s"%(l[6],l[7],l[8]))
                    break
                else : 
                    print("wrong instruction,try again")
                    continue        
            w1 = (l[0] == l[1] == l[2] == "X")
            w2 = (l[3] == l[4] == l[5] == "X")
            w3 = (l[6] == l[7] == l[8] == "X")
            w4 = (l[0] == l[3] == l[6] == "X")
            w5 = (l[1] == l[4] == l[7] == "X")
            w6 = (l[2] == l[5] == l[8] == "X")
            w7 = (l[0] == l[4] == l[7] == "X")
            w8 = (l[2] == l[4] == l[6] == "X")          
            if w1 or w2 or w3 or w4 or w5 or w6 or w7 or w8:
                print("P2 win!")
                break      
            if " " not in set(l):
                print("平手")
                break

#第九組
import random

def team9() :
    while (True) :
        listb04 =  [0,1,2,3,4,5,6,7,8,9]
        answer = random.sample(listb04, 4)    
        while True :
            I = int(input("input the 1st number"))
            II = int(input("input the 2nd number"))
            III = int(input("input the 3rd number"))
            IV = int(input("input the 4th number"))
            guess = [I, II ,III, IV]
            if len(set(guess)) != 4 :
                print("87???")
                continue
            for i in guess:
                yesorno = 0 <= i <=9
                if yesorno == False :
                    break
            if yesorno == False:
                print ("db2??")
                continue
            
            if guess == answer:
                print ("Congratulation, type anything to continue ")
                break
            else:
                a = 0
                for i in range(0,4) :
                    if answer[i] == guess[i]:
                        a += 1
                b = len(set(answer) & set(guess)) - a
                print ('%dA%dB, keep going' % (a, b))
                continue
        K = input()
        if K != "quit" :
            continue
        else:
            break
#第十組
def team10():
    for x in range(10):
        for y in range(10):
            if x*y < 10:
                print(" %s"%(x*y), end=" ")
            else:
                print(x * y, end=" ")
        print()

#第十二組
import string

def team12(anumber):
    AList =  string.digits + string.ascii_uppercase + string.ascii_lowercase
    ADic = {}
    BDic = {}
    power = 0
    Acounter = 0
    Bcounter = 0
    value = 0
    BList = []

    remainder = ""
    for n in anumber:
        BList.append(n)
    list.reverse(BList)

    for i in AList:
        ADic[i] = Acounter
        Acounter += 1
    for i in AList:
        BDic[Bcounter] = i
        Bcounter += 1
#建立以值為名以代號為值的字典
#以及以代號為名以數值為值的字典
    while True:
        a = int(input("m = ?"))
        TorF = False
        if a>=62 or a<=1 :
            print("db2??")
            continue
        else:
            for j in BList:
                if int(ADic[j]) >= a :
                    TorF = TorF or True
                else:
                    value += int(ADic[j])*(a**power)
                    power+=1
        if TorF == True:
            print("看來你只有0.87個癢 再給你一次機會")
            continue
        else:
            break
#先判斷是否有進位法不在範圍
#再判斷輸入之進位法是否能表示要被轉換之數            
    while True:
        b = int(input("n = ?"))
        if 1<b<62 :
            break
        else:
            print("db2??")
    while value > 0 :
        remainder = BDic[value%b] + remainder
        value = value // b
    print(remainder)        

#第十三組
def team13():

    total = ["000","100","200","300","400","500","600","700","800","900"]
    S = [3,2,4,1,8,9]
    L = [5,6]
    T = [7,0]
    sir = [(1,2),(1,3),(8,2),(2,3),(9,4),(9,3),(4,3),(6,5)]
    name = ["non","Jon Snow","Robert Stark","Eddard Stark","Bran Stark","Tywin Lannister","Jamie Lannister","Rhaegar Targaryen","Ser Rodrik","Hodor"]
    while True:
        x = input ("請輸入代碼1:")
        y = input ("請輸入代碼2:")    
        a = int(int(x) / 100)
        b = int(int(y) / 100)    
        if x not in total or y not in total or x == y:
            print("87")
            continue
            
        else:    
            if a in S and b in S or a in T and b in T: 
                if (a,b) in sir:
                    print("%s是%s的屬下"%(name[a],name[b]))
                elif (b,a) in sir:
                    print("%s是%s的長官"%(name[a],name[b]))
                else:
                    print("%s與%s是平輩"%(name[a],name[b]))
            if a in T or b in T:
                print ("資料有誤無法比對")
            else:
                print ("%s與%s是敵人"%(name[a],name[b]))
            break

#第十四組
import random 

def team14():
    listABC =  []
    for i in range(0,49) : 
        listABC.append(i+1)
    n = int(input("How many answers do you need?"))
    for i in range(n):
        answer = random.sample(listABC, 6)
        print(answer)
    
if __name__ == '__main__':
    n=int(input("你要執行第幾組?"))
    if n == 1:
        team1()
    if n == 2:
        team2()    
    if n == 3:
        friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}))
        friends2 = Friends(({"1", "2"}, {"2", "4"}, {"1", "3"}))
        print(friends.names())
        print(friends.connected("d"))
        print(friends.connected("a"))
        print(friends2.names())
        print(friends2.connected("1"))   
    if n == 4:
        team4()    
    if n == 5:
        xdata=[1,6,8,4,5,2,3,5]
        ydata=[4,9,3,5,4,2,6,7]
        team5(xdata,ydata)
    if n == 6:
        team6()
    if n == 7:
        team7()    
    if n == 8:
        team8()    
    if n == 9:
        team9() 
    if n == 10:
        team10()    
    if n == 12:
        testSTR = "16ZEQBA"
        team12(testSTR)        
    if n == 13:
        team13()    
    if n == 14:
        team14()  
        
    if n>14 or n<0 or n==11 :
        print("87??")