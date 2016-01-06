#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Team01

def CommonDivisor(n):
    for i in range(1,n+1):
        if n%i == 0:
            print(i)
    return None

#Team02
def Pig_Latin(n):
    list1=list(n)
    leng=len(n)
    temp=list1[0]
    for i in range(leng-1):
        list1[i]=list1[i+1]
        if (ord(list1[i])<92): list1[i]=chr(ord(list1[i])+32)
    list1[leng-1]=temp
    if (ord(list1[leng-1])<92): list1[leng-1]=chr(ord(list1[leng-1])+32)
    n=''.join(list1)+'ay.'
    return n

#Team03
class Friends:
    def __init__(self, connections):
        self.connections=connections
    def names(self):
        length=len(self.connections)
        for i in range(length-1):
            n=self.connections[i]|self.connections[i+1]
        n=list(n)
        n.sort()
        return n
    def connected(self, connections):
        n=set(connections)
        n1=set()
        for i in self.connections:
            if(i.issuperset(n)):
                n1.update(i.symmetric_difference(n))
        return n1
#Team05
def linear_least(xdata,ydata):
    x_ave=sum(xdata)/len(xdata)
    y_ave=sum(ydata)/len(ydata)
    b1=0
    b2=0
    for i,j in zip(xdata,ydata) :
        b1=b1+(i-x_ave)*(j-y_ave)
        b2=b2+(i-x_ave)*(i-x_ave)
    b=b1/b2 
    a=y_ave-b*x_ave
    return b,a
#Team06
def sigma(inputList):
    result=0
    average=sum(inputList)/len(inputList)
    for i in range(0,len(inputList)):
        result+=(inputList[i]-average)*(inputList[i]-average)
    result=result/len(inputList)
    result=result ** 0.5
    return result
#Team7
entry = input('輸入一個正整數 n ( 0 < n < 11 ):')
enternum=input("請輸入n位數字: ")       

def outTable(n,inSTRn): 

    outSTRn=""
    nn=1
    for i in range(1,n+1):

        nn=nn * i
    print("input=",n)        
    print("input=",inSTRn)
    print("output "+str(n)+"!=",nn)
    inListn=list(inSTRn)
    return inListn

COUNT=0
def perm(num_list,begin,end):
    out=""
    global COUNT
    if begin>=end:

        for num in num_list:
            out=out+" "+str(num)
        COUNT +=1
        print(out)
    else:
        i = begin
        for num in range(begin,end):
            num_list[num],num_list[i]=num_list[i],num_list[num]
            perm(num_list,begin+1,end)
            num_list[num],num_list[i]=num_list[i],num_list[num]
#Team8
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
#Team9
import random
import os
ST=[]
t=0
while t<4 :
    tem=str(random.randrange(0,9))
    if not (tem in ST):
        ST.append(tem)
        t+=1

time=1
while True:
    print u"猜第%d次。\n請輸入一個不重覆的四位數字或輸入'STOP'以退出遊戲:" %time
    A=0
    B=0
    input_s=raw_input()
    if "STOP" in input_s.upper():
        print u"離開遊戲! 正確答案為 %s" % "".join(str(n) for n in ST)
        break
    else:
        try:
            int(input_s)   
            if "".join(str(n) for n in ST)==input_s: 
                print u"Congratulation☺, press anything to continue" %time
                break
            elif len(input_s) != 4:
                print u"錯誤! 不正確的長度!\n"
            else:  
                for tem in range(4):
                    if ST[tem] == input_s[tem]: 
                        A+=1
                    if input_s[tem] in ST: 
                        B+=1
                print "%d A\t%d B" % (A,B-A)
                time+=1
        except:
            print u"錯誤! 內含非數字的字串\n"
os.system("pause")
#Team10

for i in range(0,10):
    for c in range(0,10):
        if i*c < 10:
            print(i*c,end='')
            print("  ",end='')
        else:
            print(i*c,end='')
            print(" ",end='')
    print( )
#Team_11
def team11():
	y = 0
	while y == 0: 
	    PlayerLIST = []
	    Function = []
	    n = 10
	    i = 0
	    
	    while n > 5 or n < 2:
	        if i == 0:
	            n = input("請輸入玩家數（限2至5名）：")
	        else:
	            n = input("請重新輸入玩家數（限2至5名）：")
	        if n.isdigit() == True:
	            n = int(n)
	        i += 1
	    print("") 
	    
	    i = 0
	    x = 0
	    while i < n:
	        print("請輸入玩家",i+1, "名稱：")
	        Name = input()
	        while i > x:
	            x += 1
	            if Name == PlayerLIST[x*2-1]:
	                print("不允許玩家同名！")
	                Name = input("請重新輸入玩家名稱：")
	                x = 0
	        x = 0
	        PlayerLIST.append(i+1)
	        PlayerLIST.append(Name)
	        Function.append(Name)
	        Function.append(1)
	        Function.append(1)
	        i += 1
	    print("") 
	    
	    import random
	    j = random.randint(0,n-1)
	    z = j*2+1
	    Function[3*j+1] = 0
	    Function[3*j+2] = 0
	    print ("以下數字只有玩家",PlayerLIST[z],"能看")
	    print ("按下enter後看數字")
	    m = input("")
	    w = random.randint(1,36)
	    print(w)
	    print("往後的輸入皆由",PlayerLIST[z],"操作")
	    print("")
	    
	    N = 1
	    r = 1
	    Bingo = 0
	    inputLIST = ["1","2","3","return","pass"]
	    while w > Bingo:
	        print("目前數字為：",Bingo)
	        print("請玩家",PlayerLIST[2*N-1],"選擇1至3的其中一數字：")
	        print("(提醒您：此玩家尚有",Function[3*N-2],"次return功能牌",Function[3*N-1],"次pass功能牌)")
	        a = input("")
	        while a not in inputLIST:
	            print ("輸入錯誤！請重新輸入：")
	            a = input("")
	        while inputLIST.index(a) == 3 and Function[3*N-2] == 0:
	            print ("此玩家已經沒有return的功能牌了！請重新輸入：")
	            a = input("")   
	        while inputLIST.index(a) == 4 and Function[3*N-1] == 0:
	            print ("此玩家已經沒有pass的功能牌了！請重新輸入：")
	            a = input("")    
	        print("")
	        if inputLIST.index(a) < 3:
	            Bingo += int(a)
	        elif inputLIST.index(a) == 3:
	            Function[3*N-1] = 0
	            Function[3*N-2] = 0
	            r = -r
	        elif inputLIST.index(a) == 4:
	            Function[3*N-1] = 0
	            Function[3*N-2] = 0
	        if w > Bingo:
	            A = N        
	        N += r
	        if N > n:
	            N -= n
	        if N < 0:
	            N += n
	            
	    print ("玩家",PlayerLIST[2*A-1],"lost the game!")
	    print("")
#Team12
def index():
    alllist = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    newlist = []
    j = 0
    for i in alllist:
        newlist.append((i,j))
        j = j+1
    return newlist

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

def team12(inputSTR,a,b):
    
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


#Team13
def team13():

    total = ["000","100","200","300","400","500","600","700","800","900"]
    S = [3,2,4,1,8,9]
    L = [5,6]
    T = [7,0]
    sir = [(1,2),(1,3),(8,2),(2,3),(9,4),(9,3),(4,3),(6,5)]
    name = ["non","Jon Snow","Robert Stark","Eddard Stark","Bran Stark","Tywin Lannister","Jamie Lannister","Rhaegar Targaryen","Ser Rodrik","Hodor"]
    while True:
        x = input ("請輸入第一人代碼:")
        y = input ("請輸入第二人代碼:")    
        a = int(int(x) / 100)
        b = int(int(y) / 100)    
        if x not in total or y not in total or x == y:
            print("There's something wrong!")
            continue
            
        else:    
            if a in S and b in S or a in T and b in T: 
                if (a,b) in sir:
                    print("%s是%s的屬下"%(name[a],name[b]))
                elif (b,a) in sir:
                    print("%s是%s的長官"%(name[a],name[b]))
                else:
                    print("%s與%s是平輩"%(name[a],name[b]))
            elif a in T or b in T:
                print ("資料有誤無法比對")
            else:
                print ("%s與%s是敵人"%(name[a],name[b]))
            break
			
#Team14
def team14(inputSTR):
    import random
    RList=[]
    T=int(inputSTR)
    i = 0
    while i < T:
        a=random.sample(range(1,49),6)
        RList.append(a)
        i += 1
    return RList
    
if __name__ == "__main__":
    
    print("Team01:")
    n=input("Please input a number:")
    CommonDivisor(int(n,10))    
    
    print("Team02:")
    str=input("Please input a word in English:")
    while(True):
        Is=True
        for i in str:
            if  not((ord(i)>96 and ord(i)<124) or (ord(i)>64 and ord(i)<92)):
                str=input("Input false.Please input a string only in English:")
                Is=False
                break
        if(Is): break
    print(Pig_Latin(str))
    
    print("Team03:")
    friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}))
    friends2 = Friends(({"1", "2"}, {"2", "4"}, {"1", "3"}))    
    print("friends.names==%s"%friends.names())
    print("friends.connected(\"d\")=%s"%friends.connected("d"))
    print("friends.connected(\"a\")=%s"%friends.connected("a"))
    print("friends2.names==%s"%friends2.names())
    print("friends2.connected(\"1\")=%s"%friends2.connected("1"))
    
    print("Team05:")
    xdata=[1,6,8,4,5,2,3,5]
    ydata=[4,9,3,5,4,2,6,7]
    b,a=linear_least(xdata,ydata)
    print ("y=%.4fx+%.4f"%(b,a))
    
    
    inputList=[40,50,60]
    print(sigma(inputList))    
    
    
    
    YO=input("please enter a number:")
    print(team14(YO))    
    print("Team11:")
	team11()  
	
	
    print("Team12:")
    t12a = int(input("進位m>>>"))
    t12b = int(input("進位n>>>"))
   # print(translater("16ZEQBA"))
    print(team12("16ZEQBA",t12a,t12b))  
	
	
    print("Team13:")
	team13()
    
    
    
    
    
    
 