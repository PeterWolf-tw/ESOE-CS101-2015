#!/usr/bin/env python 3
#-*- coding:utf-8 -*-
#設計一個程式
#若使用者輸入一個數值
#可算出該數值所具有的所有公因數
#例如輸入633
#可得1 3 211 633

def mathfunction(n):
    resultlist = []
    i = 1
    
    k = n    
    
    while i <= k:
        remain = n % i
        if remain == 0:
            resultlist.append(i)
            resultlist.append(-i)
        i = i + 1
        
        
   
    resultlist.sort
   
    return resultlist
    
#if __name__ == "__main__":
    
#    n=633
#    result=mathfunction(n)
    
 #   print(result)


 '''
 題目內容:
 Pig Latin is a language game, 
 where you move the first letter of the word to the end 
 and add "ay." So "Python" becomes "ythonpay." 
 
 說明:
 1.Ask the user to input a word in English.
 2.Make sure the user entered a valid word.
 3.Convert the word from English to Pig Latin.
 4.Display the translation result.
 '''
 
def PigLatin(word):
    fixword = word.isalpha()   
    if fixword == True:
        x = word[0]
        y = len(word)
        word1 = word[1:y]
        word1 = word1 + x + 'ay.'
        return word1
    else:
        return ('invalid word')
 
word = input('Please insert an English word: ')
print(PigLatin(word))
  
  

#針對一個class Friends
#定義names 和 connected
#舉例如主程式後
#特別注意:在class裡{"a", "b"}和{"b", "a"}並無不同
# names 是舉出所有出現在Friends裡的"名字",不重複
# connected(a) 是舉出所有在Friends裡 和a有關的名字    


class Friends:  

    def __init__(self, name, coname):
        self.name   = name  
        self.coname = coname  

    def names():
        nameList=[]
        for i in Friend:
            nameList.append(i.name)
            nameList.append(i.coname)
            sortList = sorted(nameList)           
            length = len(sortList)                

            remainList =[]                        
            remainList.append(sortList[0])        
            wkchar = str(sortList[0])             

            for i in range(0,length):             
                if wkchar != str(sortList[i]):     
                    wkchar = str(sortList[i])
                    remainList.append(sortList[i])

        nameset=set(remainList)
        print('所有的名字:',nameset)              


    def connected(inname):
        length=0
        innameset={inname}
        connList=[]
        for i in Friend:
            if i.name==inname or i.coname==inname:
                connList.append(i.name)
                connList.append(i.coname)

                sortList = sorted(connList)           
                length = len(sortList)             

                remainList =[]                       
                remainList.append(sortList[0])        
                wkchar = str(sortList[0])            

                for i in range(0,length):           
                    if wkchar != str(sortList[i]):     
                        wkchar = str(sortList[i])
                        remainList.append(sortList[i]) 

        if length == 0:
            connset={}
        else:
            connset=set(remainList)-innameset
        connList=sorted(connset)
        print(bb,'的朋友:',connset)                



#if __name__ == '__main__': 

    #friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"})) 
    #friends2 = Friends(({"1", "2"}, {"2", "4"}, {"1", "3"})) 

    # friends.names() == {"a", "b", "c"}, "Names" 
    # friends.connected("d") == set(), "Non connected name" 
    # friends.connected("a") == {"b", "c"}, "Connected name" 
    # friends2.names() == {"1", "2", "3", "4"} 
    # friends2.connected("1") == {"2", "3"}

#    Friend=[]
#    Friend.append( Friends('a', 'b') )
 #   Friend.append( Friends('b', 'c') )
#    Friend.append( Friends('c', 'a') )
#    Friends.names()

#    bb="a"
#    Friends.connected(bb)

#    bb="d"
#    Friends.connected(bb)

#########################################################################
#    Friend=[]
#    Friend.append( Friends('1', '2') )
#    Friend.append( Friends('2', '4') )
#    Friend.append( Friends('1', '3') )
#    Friends.names()

#    bb="1"
#    Friends.connected(bb)

#    bb="4"
#    Friends.connected(bb)

#    bb="0"
#    Friends.connected(bb)


    #設計一個程式 
    #若input=n 
    #可算出費式數列第n項的值 
    #費式數列第n項的值等於第(n-1)項與第(n-2)項的和 
    #且a1=a2=1 
    
    
def fib(n): 
    if n <= 1:         
        return n       
    else:              
        return fib(n - 1) + fib(n - 2)
    
#if __name__ == "__main__":
#    n=6
#    fibn=fib(n)
#    print("費式數列(" + str(n) + ")=" + str(fib(n)))


#This is question designed by us.
#It's not very hard.
#!It is about the linear least squares.
#We will give a bunch of xdata and ydata.
#!The only thing you have to do is to give the equation in the form of "y = ax + b" by using linear least squares method
#!AS for the number of data is determined by us, so you can use while loop or for loop with range
#Don't use anything such as numpy, scipy or whatever.
#I can't test the program without the package.
#Don't try to connect to the Wolframalpha or Matlab.
#I will test it without internet.
#You can surely copy other classmates' codes, but make sure each other's willingness.
#Or your codes will be regard as copy one, though you will still get the points.

#!xdata and ydata are both lists
#!for example, xdata=[1,6,8,4,5,2,3,5], ydata=[4,9,3,5,4,2,6,7]
#!we want the result in string "y = 0.2535x + 3.9225
#"
#!for our convenience, please use  if __name__== "__main__":
#! MIND IT ! THE PERCISION NEED TO BE AT LEAST E-4(10^-4)

import math

def SXX(listX):
    squareX = []
    n = len(listX)
    Xbar = sum(listX)/n
    for x in range(0,n):
        squareX.append(int(listX[x])**2)
        sumX = sum(squareX)                
        SXX = sumX - n*(Xbar**2)
    return SXX

def SXY(listX,listY):
    listXY = []
    n = len(listX)
    Xbar = sum(listX)/n
    Ybar = sum(listY)/n
    for x in range(0,n):
        listXY.append(int(listX[x])*int(listY[x]))
        sumXY = sum(listXY)
        SXY = sumXY - n*Xbar*Ybar    
    return SXY

#if __name__== "__main__":
#    listX = [1,6,8,4,5,2,3,5]
#    listY = [4,9,3,5,4,2,6,7]
#    n = len(listX)
#    SXXX = SXX(listX)
#    SXYY = SXY(listX,listY)
#    Xbar = sum(listX)/n
#    Ybar = sum(listY)/n    
#    m = SXYY/SXXX
#    a = m
#    b = Ybar - m*Xbar

#    print('Xdata = {}'.format(listX))
#    print('Ydata = {}'.format(listY))
#    print("y = {}x + {}". format(a,b))
 
 
#請輕鬆設計出一個可計算出任意個實數組之表準差的函數 
# ex: input=(40,50,60) , output=8.164965809277.... 
# ex: input=(60,60,60,60) , output=0 


def SDfinder(inputSTR):
    numbers = inputSTR. split(',')
    total = 0    
    for tony in numbers:
        total += int(tony)
    average = total/len(numbers)    
    variance = 0    
    for liu in numbers:
        variance += ((int(liu) - average)**2)/len(numbers)
    SD = variance**0.5
    return SD
#if __name__ == "__main__":
#    inputSTR = input("number(s):")
#    SD = SDfinder(inputSTR)
#    print(inputSTR)
#    print(SD)


#題目內容： 
# 

# 	設計一支程式，使其在輸入一串互不相等數字之後，輸出其所有可能之排列個數及排列。 


# 輸入說明： 


# 	1.首先輸入一個正整數 n ( 0 < n < 11 )，代表接下來要輸入的數字個數。 
# 	2.接著輸入 n 個正整數 a1, a2, a3,....an ( ai != aj, where 1 < i, j < 11 and i != j )。 

# 輸出說明： 


# 	1.輸出 n!。 
# 	2.輸出此 n 個正整數 a1, a2, a3,....an 所有可能之排列。 
# 	 
# 範例輸入： 


# 	3 
# 	1 2 3 

# 範例輸出： 

# 	6 
# 	1 2 3 
# 	1 3 2 
# 	2 1 3 
# 	2 3 1 
# 	3 1 2 
# 	3 2 1 


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



#if __name__ == "__main__":
#    n=int(entry)
#    inSTRn=enternum
#    num_list=outTable(n,inSTRn)
#    perm(num_list,0,n)
#    print("Total: %s" % COUNT)


#請設計一個兩人對戰的圈圈叉叉遊戲
#利用|與—畫出圈圈叉叉的九宮格圖形
#如果你覺得設計兩人對戰的遊戲是小蛋糕一塊
#你也可以選擇設計玩家與電腦對戰的圈圈叉叉

class Board:

    def __init__(self, square1=' ', square2=' ', square3=' ', square4=' ', square5=' ', square6=' ', square7=' ', square8=' ', square9=' '):
        self.square1 = square1
        self.square2 = square2
        self.square3 = square3
        self.square4 = square4
        self.square5 = square5
        self.square6 = square6
        self.square7 = square7
        self.square8 = square8
        self.square9 = square9

    def grid(self):
        message = '\n數字0到8, 從左上到右下, 水平排列\n   |   |   \n ' + self.square1+' | '+self.square2+' | '+self.square3+'  \n___|___|___\n   |   |   \n '+self.square4+' | '+self.square5 + ' | ' + self.square6+'  \n___|___|___\n   |   |   \n ' + self.square7 + ' | ' + self.square8+' | ' + self.square9+'  \n   |   |   '
        print(message)
        a=""
        return a


game=Board()

print(game.grid())

count=0
sw1_do="Y"                                        
sw2_do="Y"                                        
allnum={'0','1','2','3','4','5','6','7','8'}      
inset=set()                                        
X1row=""
X2row=""
X3row=""
X1col=""
X2col=""
X3col=""
X1slo=""
X2slo=""
O1row=""
O2row=""
O3row=""
O1col=""
O2col=""
O3col=""
O1slo=""
O2slo=""

while True:
    sw1="Y"                                      
    sw2="Y"                                       
    if sw1_do == "Y":
        entry = input('  X 上場,請輸入 0-8 的數字, <Ctrl>C to quit\n')
        entryx=int(entry)
        if entryx in(0,1,2,3,4,5,6,7,8):
            remainList = list(allnum)
            for i in remainList:
                if i == entry:                    
                    sw1=""                     
        else:
            sw1="Y"

        if sw1 == "" and sw1_do == "Y":
            inset.add(entry)
            allnum = allnum - inset               
            count += 1
            if entry == '0':
                game.square1='X'

            elif entry == '1':
                game.square2='X'

            elif entry == '2':
                game.square3='X'

            elif entry == '3':
                game.square4='X'

            elif entry == '4':
                game.square5='X'

            elif entry == '5':
                game.square6='X'

            elif entry == '6':
                game.square7='X'

            elif entry == '7':
                game.square8='X'

            elif entry == '8':
                game.square9='X'

            print(game.grid())

        if sw1 == "Y":
            sw1_do="Y"
            sw2_do="N"                    
            print("錯誤, 重新輸入:\n")
        else:
            sw1_do="N"
            sw2_do="Y"

    if game.square1 == game.square2 == game.square3 == 'X':
        X1row = 'Y'
    if game.square4 == game.square5 == game.square6 == 'X':
        X2row = 'Y'
    if game.square7 == game.square8 == game.square9 == 'X':
        X3row = 'Y'
    if game.square1 == game.square4 == game.square7 == 'X':
        X1col = 'Y'
    if game.square2 == game.square5 == game.square8 == 'X':
        X2col = 'Y'
    if game.square3 == game.square6 == game.square9 == 'X':
        X3col = 'Y'
    if game.square1 == game.square5 == game.square9 == 'X':
        X1slo = 'Y'
    if game.square3 == game.square5 == game.square7 == 'X':
        X2slo = 'Y'
    if X1row=='Y' or X2row=='Y' or X3row=='Y' or X1col=='Y' or X2col=='Y' or X3col=='Y' or X1slo=='Y' or X2slo=='Y':
        print("  X 成功,遊戲結束!")
        break

    if count > 8:
        print("遊戲結束!")
        break

    if sw2_do == "Y":
        entry2 = input('換 O, 請輸入 0-8 的數字, <Ctrl>C to quit\n')
        entryy=int(entry2)

        if entryy in(0,1,2,3,4,5,6,7,8):
            remainList = list(allnum)
            for i in remainList:
                if i == entry2:                   
                    sw2=""                       
        else:
            sw2="Y"

        if sw2 == "" and sw2_do == "Y":
            count += 1
            inset.add(entry2)
            allnum = allnum - inset              
            if entry2 == '0':
                game.square1='O'

            elif entry2 == '1':
                game.square2='O'

            elif entry2 == '2':
                game.square3='O'

            elif entry2 == '3':
                game.square4='O'

            elif entry2 == '4':
                game.square5='O'

            elif entry2 == '5':
                game.square6='O'

            elif entry2 == '6':
                game.square7='O'

            elif entry2 == '7':
                game.square8='O'

            elif entry2 == '8':
                game.square9='O'

            print(game.grid())

        if sw2 == "Y":
            sw2_do="Y"
            sw1_do="N"                    
            print("錯誤, 重新輸入:\n")
        else:
            sw1_do="Y"
            sw2_do="N"

    if game.square1 == game.square2 == game.square3 == 'O':
        O1row = 'Y'
    if game.square4 == game.square5 == game.square6 == 'O':
        O2row = 'Y'
    if game.square7 == game.square8 == game.square9 == 'O':
        O3row = 'Y'
    if game.square1 == game.square4 == game.square7 == 'O':
        O1col = 'Y'
    if game.square2 == game.square5 == game.square8 == 'O':
        O2col = 'Y'
    if game.square3 == game.square6 == game.square9 == 'O':
        O3col = 'Y'
    if game.square1 == game.square5 == game.square9 == 'O':
        O1slo = 'Y'
    if game.square3 == game.square5 == game.square7 == 'O':
        O2slo = 'Y'
    if O1row=='Y' or O2row=='Y' or O3row=='Y' or O1col=='Y' or O2col=='Y' or O3col=='Y' or O1slo=='Y' or O2slo=='Y':
        print("  O 成功啦,遊戲結束!")
        break


#試設計一個可以猜數字的程式， 
#此程式必須先隨機產生四個不重複的數字， 
#其input為四位數字， 
#output為“number,A,number,B”（A=數字相同位置也相同，B=數字相同位置不同）， 
#當出現4A0B時，即顯示“Congratulation☺, press anything to continue  ”， 
#遊戲重複。 





print("Attention: The numbers must be between 0 and 9")
import random
answerLIST = []
a = 0
while a <= 3:
    number = random.randrange(0,9)
    if number not in answerLIST:
        answerLIST.append (number)
        a += 1
print(answerLIST)
    
guessLIST = []
ABLIST = []
ALIST = []
ACOUNT = str(ABLIST). count("A")
b = 1
    
while b <= 4:
    guess = int(input("Enter the number right here: "))
    if guess not in guessLIST and 0 <= guess <= 9:
        guessLIST.append (guess)
        b += 1
    else:
        print("INVALID")
print("The numbers you guessed are {}". format(guessLIST))
ABLIST = []
c = 0
for number in guessLIST:
    if number == answerLIST[c]:
        ABLIST.append("A")
    elif number != answerLIST[c] and number in answerLIST:
        ABLIST.append("B")
    c += 1
print(ABLIST)
print("{}A{}B". format((str(ABLIST). count("A")),str(ABLIST). count("B")))


#   請設計一個程式能自動列出九九乘法表如下(每行要對齊): 


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


def MutiTable(): 
    strX=""
    strY=""    
    for j in range(0,10):             
        for i in range(0,10):
            k = j * i
            if k < 10:
                strX = " "+str(k)     
            else:
                strX = str(k)
            strY = strY + " " + strX  
        print(strY)                 

        print()                                  
        strY = ""                     


#if __name__ == "__main__":
#    result = MutiTable()

       
#猜數字遊戲

#參賽者2~5人,先各自輸入名字,電腦隨機擇一範圍在1~36內的數字,並隨機擇一玩家可知曉該數字,開始遊戲.
#各玩家按順序喊+1~+3,除知曉數字的人以外各玩家可使用功能牌:pass or return一次,持續到有一玩家喊到或經過設定的數字者為輸.可重複遊戲.
#需該回合玩家知道她可輸入得指令 e.x: 玩家___,你可輸入數字1~3 or pass or return

import random 

class Person:  
    def __init__(self, num, name, pchk, rchk):  
        self.num = num  
        self.name = name  
        self.pchk = pchk  
        self.rchk = rchk

    def set_num(self, num):  
        self.num = num

    def set_pchk(self, pchk):  
        self.pchk = pchk

    def set_rchk(self, rchk):  
        self.rchk = rchk  

def gamestart():

    persons=[]
    n=input('請輸入參賽人數2~5: ')
    n= int(n)
    for i in range(0,n):
        j = i + 1
        entername=input('請玩家輸入名字:')  
        persons.append( Person(j,entername, 'Y', 'Y') )
        print('第 ',i+1,' 號玩家名字是 ',entername)
    print()

    number=0
    ranint= random.randint(1,36)
    rannum= random.randint(1,n)       
    print('電腦隨機取得的數字: ',ranint)

    for i in persons:
        if i.num == rannum:
            persons[i.num-1].set_pchk('N')    
            persons[i.num-1].set_rchk('N')
            print('可看數字的玩家是: ',rannum,'號 ', i.name)

            print()
            print()
    return number, ranint, persons, n

def enternum(num,name,pchj,rchk):
    error="Y"
    if pchk == 'Y':
        Msgp=' or pass'
    else:
        Msgp=''
    if rchk == 'Y':
        Msgr=' or return'
    else:
        Msgr=''
    while error=="Y":
        enternums=input('玩家 '+str(num)+' 號 '+name+' 請輸入1~3數字'+Msgp+Msgr+' :') 
        if enternums.isalpha():
            words = enternums.lower()
            if (words == 'pass' and pchk == 'Y') or (words == 'return' and rchk == 'Y'):

                error="N"
                if words == 'pass':
                    enternums = 0

                if words == 'return':
                    enternums = -1

            else:
                print('輸入錯誤, 請重新輸入')
        else:
            if int(enternums) <= 0 or int(enternums) > 3:
                print('輸入錯誤, 請重新輸入')
            else:
                error="N"

    return int(enternums)


if __name__ == '__main__':

    number,ranint,persons,n=gamestart()

    while number < ranint:
        ii=0
        persons.sort(key=lambda i: i.num) 
        for i in persons:
            if ii < 10:

                num =i.num
                name=i.name
                pchk=i.pchk
                rchk=i.rchk
                enternums=enternum(num,name,pchk,rchk)
                if enternums > 0:
                    number += enternums
                else:
                    if enternums == 0:
                        persons[num-1].set_pchk('N')
                    else:
                        persons[num-1].set_rchk('N')
                        npersons=[]
                        for j in persons:
                            if j.num < num: 
                                npersons.append(Person(j.num,j.name,j.pchk,j.rchk))
                                print(j.num,j.name,j.pchk,j.rchk)   
                            elif j.num > num:
                                npersons.append(Person(j.num-1,j.name,j.pchk,j.rchk))
                                print(j.num-1,j.name,j.pchk,j.rchk)   
                            else:
                                npersons.append(Person(n,j.name,j.pchk,j.rchk))
                                print(n,j.name,j.pchk,j.rchk)   
                        ii = 10

                print('total=',number)
                if number >= ranint:
                    print(num,"號",name,"輸了")
                    print('電腦隨機取得的數字是: ',ranint)
                    #break
                    print()
                    print()
                    print('遊戲重新開始!')
                    ii = 11
                    number,ranint,persons,n=gamestart()
        if ii == 10:
            persons=npersons


#請參考以下空白程式，設計一支程式能將輸入的字串定義為m進位法，並且換算成n進位法(其中，m, n為介於2至61的正整數)
#在此，我們定義大寫英文字母A為10、Z為35;小寫英文字母a為36、z為61，其他字母以此類推
#可不考慮負數及浮點數的計算





def M10(x):
    result = 0
    table = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    i = 0
    n = len(x)
    while  i <= len(x)-1:
        result = result + int(table.find(x[i]))*m**(n-1)
        i += 1
        n -= 1     
    return result      

def N10(num):
    result = ''
    table = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    while num >= n:
        result =   table[num%n] + result
        num = num//n
        if num < n:
            result = table[num] + result
        
    return result  

x = input('Just insert anything you want: ')
m = int(input('Please insert a number between 2 and 61: '))
n = int(input('Please insert a number between 2 and 61: '))
num = M10(x)
print(M10(x))
print(N10(num))





#我們得題目很簡單
#就是做一個樂透開獎程式
#多組號碼49選6
#輸入數字n
#便會跑出n組1~49中隨機挑選的六個數字

import random 

def lottery(x):
    list1to49=list(range(1,50)) 
    lotterynum = []
    y = int(x)
    while y>0:
        lotterynum.append(random.sample(list1to49,6))
        y -= 1
    return lotterynum  
  

x = input('please insert a number: ')
print(lottery(x))














