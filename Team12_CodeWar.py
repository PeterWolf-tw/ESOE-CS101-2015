#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#Team_01
def GCD(x):
    numberLIST=[]
    j=1
    while j<=int(x):
        if int(x)%j==0:
            numberLIST.append(j)
            numberLIST.append((-1)*j)
        j+=1
    return numberLIST
if __name__== "__main__":
    a = input("請輸入一正整數：")
    while str(a).isdigit() != True or a =="0":
        a = input("請重新輸入一正整數：")
    a = int(a)
    print(GCD(a))

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#Team_02
def main(x):
    i = 1
    result = ""
    while  x.isalpha() != True:
        STR = input("請重新輸入英文字母：")
    while i < len(x):
        result = result + x[i]
        i += 1
    result = result + x[0] + "ay."
    return result
        
if __name__ =="__main__":
    STR = input("請輸入英文字母：")
    print (main(STR))

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#Team_03
class Friends:
    i=0
    def __init__(self, connections):
        self.connections=connections
        Friends.i += 1    
            
    def names(self):
        k=0
        sum=self.connections[0]
        for k in range(len(self.connections)):
            sum=sum|self.connections[k]
        print(sum)       
        

    def connected(self, connections):
        k=0
        j=0
        con={connections,""}
        sum=set()
        for k in range(len(self.connections)):
            if con&self.connections[k]==set():
                continue
            elif j==0:               
                sum=self.connections[k]-con
                j+=1
            else:
                sum=sum|(self.connections[k]-con)
        if sum==set():
            print("Non connected name!")
        else:
            print(sum)

if __name__ == '__main__':

    friends_object=[]
    friends_object.append(Friends(({"a", "b"}, {"b", "c"}, {"c", "a"})))
    friends_object.append(Friends(({"1", "2"}, {"2", "4"}, {"1", "3"})))
    print(len(friends_object))
    i=0
    while i in range(len(friends_object)):
        print("group ",i," = ",end='')
        friends_object[i].names()
        i+=1
    group=int(input("Please choose a group:"))
    name=input("Please enter a name:")
    friends_object[group].connected(name)

#!/usr/bin/env python3     
# -*- coding:utf-8 -*-
#Team_04
def Fibonacci(k):
    if k == 1:  
        return 1
    elif k == 2:
        return 1
    else:  
        return Fibonacci(k-1) + Fibonacci(k-2)

if __name__== "__main__":
    n = input("輸入費氏數列第n項:")
    while str(n).isdigit() != True or str(n) == "0":
        n = input("請重新輸入n值:")
    n = int(n)
    print (Fibonacci(n))

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#Team_05
def averagex(x):
    h=len(x)
    j=0
    sum=0
    while j<h:
        sum=sum+int(x[j])
        j=j+1
    bruce=sum/float(h) 
    return bruce
def averagey(y):
    r=len(y)
    s=0
    summ=0
    while s<r:
        summ=summ+int(y[s])
        s=s+1
    bruce2=summ/float(r) 
    return bruce2
def standard(x):
    h=len(x)
    j=0
    sum=0
    while j<h:
        sum=sum+int(x[j])
        j=j+1
    average=sum/float(h)  
    q=0
    sum2=0
    while q<h:
        sum2=sum2+(int(x[q])-average)**2
        q=q+1
    answer=(sum2/float(h))**0.5
    return answer
def standard2(y):
    r=len(y)
    s=0
    summ=0
    while s<r:
        summ=summ+int(y[s])
        s=s+1
    average2=summ/float(r)  
    w=0
    summ2=0
    while w<r:
        summ2=summ2+(int(y[w])-average2)**2
        w=w+1
    answer2=(summ2/float(r))**0.5
    return answer2
def r(x,y):
    h=len(x)
    j=0
    sum=0
    while j<h:
        sum=sum+int(x[j])
        j=j+1
    average=sum/float(h)  
    q=0
    sum2=0
    while q<h:
        sum2=sum2+(int(x[q])-average)**2
        q=q+1    
    r=len(y)
    s=0
    summ=0
    while s<r:
        summ=summ+int(y[s])
        s=s+1
    average2=summ/float(r)  
    w=0
    summ2=0
    while w<r:
        summ2=summ2+(int(y[w])-average2)**2
        w=w+1    
    mother=(sum2*summ2)**0.5
    
    xlist=[]
    ylist=[]
    for a in x:
        xlist.append(int(a)-average)
    for b in y:
        ylist.append(int(b)-average2)
    sum3=0
    e=0
    while e<h:
        sum3=sum3+float(xlist[e])*float(ylist[e])
        e=e+1
    R=sum3/float(mother)
    return R
if __name__== "__main__":
    x = input("請輸入一組數字（以逗號分開）：").split(",") 
    y = input("請輸入另組數字（以逗號分開）：").split(",")
    while len(x) != len(y):
        print("")
        print("兩組數據的數字數要相同！")
        x = input("請重新輸入一組數字（以逗號分開）：").split(",") 
        y = input("請重新輸入另組數字（以逗號分開）：").split(",")
    m=r(x,y)*standard2(y)/float(standard(x))
    fuck=(averagey(y)-averagex(x)*m)
    u=str(m)
    shit=str(fuck)
   
    if fuck>0:
        print("Y = "+u+"X + "+shit)
    elif fuck==0:
        print("Y = "+u+"X")
    else :
        print("Y = "+u+"X "+shit)

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#Team_06
def standard(x):
    h=len(x)
    j=0
    sum=0
    while j<h:
        sum=sum+int(x[j])
        j=j+1
    average=sum/float(h)  
    q=0
    sum2=0
    while q<h:
        sum2=sum2+(int(x[q])-average)**2
        q=q+1
    answer=(sum2/float(h))**0.5
    return answer
    
if __name__== "__main__":
    x = input("請輸入數個數字（以逗號隔開）：").split(",") 
    print(standard(x))

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#Team_07
l = int(input("請輸入要輸入的數字數："))
LIST = []
i = 0
while l < 1 or l > 10:
    print("")
    print("數字數只能介於1至10！")
    l = int(input("請重新輸入的數字數："))
while i < l:
    a = input("請輸入數字：")
    x = 0
    while x != 1:
        x = 1
        if a.isdigit() != True or a == "0":
            print("只能輸入一個正整數！")
            a = input("請重新輸入數字：")
            x = 0
        else:
            a = int(a)
        for m in range(i):
            if a == LIST[m]:
                print("不能輸入相同字元！")
                a = input("請重新輸入數字：")
                x = 0             

    LIST.append(a)
    i += 1
import itertools  
result_LIST = list(itertools.permutations(LIST,l))

ans = 1
for i in range(1,l+1,1):
    ans = ans*i
print (ans)
i = 0
while i < len(result_LIST):
    print (result_LIST[i])
    i += 1

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#Team_08
def show(list1):
    for k in range(3):
        for i in range(7):
            if i%2 != 0 :
                print("-" ,end='')
            else:
                print(" " ,end='')
        print("")
        for i in range(7):
            if i%2 == 0:
                print("|",end='')
            elif list1[k][int(i/2)]==1:
                print("O",end='')
            elif list1[k][int(i/2)]==-1:
                print("X",end='')
            else:
                print(" ",end='')
        print("")
    for i in range(7):
            if i%2 != 0 :
                print("-" ,end='')
            else:
                print(" " ,end='')
    print("")
        
def checkwin(list1):
    tide=1
    for i in range(3):
        for j in range(3):
            t=list1[i][j]
            if t==0:
                tide=0
                continue
    if tide==1:
        print("Tie!!")
        return 0
                
    for i in range(3):
        for j in range(3):
            temp=list1[i][j]
            if temp==0:
                continue
            tempi=i-1
            tempj=j-1
           ## print("i= ",i)
           ## print("tempi=",tempi)
            for tempi in range(3):
                if tempi<0 or tempi>2:
                    ##print("tempi==i")
                    continue      
                else:
                    for tempj in range(3):
                        if tempj<0 or tempj>2 or (tempj==j and tempi==i):
                            continue
                        
                        elif list1[tempi][tempj]==temp:
                            ##print("ti=",tempi)
                            idx=tempi-i
                            jdx=tempj-j
                            if tempi+idx<0 or tempi+idx>2 or tempj+jdx>2 or tempj+jdx<0:
                                continue
                            elif list1[tempi+idx][tempj+jdx]==temp:
                                if temp==1:
                                    print("'O' win!!")
                                elif temp==-1:
                                    print("'X' win!!")
                                return 0
    return 1

def fundai(list1,x,y):
    if list1[2-y][x]!=0:
        print("Please try again!")
        return False
    else:
        return True

if __name__ == '__main__':
    list1=[[0,0,0],[0,0,0],[0,0,0]]
    win=1
    x=0
    y=0
    fd=1
    while win:
        if fd == 1:        
            print("O's turn")
            x=int(input("input your x coordinate(0~2):"))
            y=int(input("input your y coordinate(0~2):"))
            if x>2 or x<0 or y>2 or y<0 or fundai(list1,x,y) == False :
                print("Please input again!")
                continue
            list1[2-y].pop(x)
            list1[2-y].insert(x,1)
            ##print(list1)
            show(list1)
            win=checkwin(list1)
            if win==0:
                break
        print("X's turn")
        x=int(input("input your x coordinate(0~2):"))
        y=int(input("input your y coordinate(0~2):"))
        if x>2 or x<0 or y>2 or y<0 or fundai(list1,x,y) == False:
            fd=0
            ##print(list1)
            continue
        list1[2-y].pop(x)
        list1[2-y].insert(x,-1)
        fd=1
        show(list1)
        win=checkwin(list1)

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#Team_09
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def OAOB(N): 
    A = 0
    B = 0 
    if len(N) != 4:
        return "輸入錯誤！"
    for i in range(len(N)):
        for j in range(len(N)):
            if N[i] == N[j] and i != j:
                return "輸入錯誤！"
            else:
                if int(N[i]) == Bingo[j] and i == j:
                    A += 1
                elif int(N[i]) == Bingo[j]:
                    B += 1
    return ("A:",A,"B:",B)
    

if __name__=="__main__": 
    m = 0
    while m == 0:
        numLIST = []
        i = 0
        while i < 10:
            numLIST.append(i)
            i += 1
        import random
        random.shuffle(numLIST)
            
        Bingo = []
        a = 0
        while a < 4:
            Bingo.append(numLIST[a])
            a += 1
        
        z = 0
        while z != 4:   
            Guess = input("請猜一個四位數：") 
            z = OAOB(Guess)[1]
            if z == 4:
                print ("Congratulation:), type anything to continue")
                a = input("")
            else:
                print (OAOB(Guess))

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#Team_10
for x in range(1,10):
    for y in range(1,10):
        if x*(y+1)>=10:
            print(x * y, end=" ")
        if x*(y+1)<10:
            print(x * y, end="  ")
    print()

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#Team_11
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
            
    print ("!!!!!玩家",PlayerLIST[2*A-1],"輸了!!!!!")
    print("")

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#Team_13
if __name__ == '__main__':
    list1=[[100,"Jon Snow",200,0],[200,"Robert Stark",300,0],[300,"Eddard Stark",300,0],[400,"Bran Stark",300,0],[500,"Tywin Lannister",500,1],[600,"Jamie Lannister",500,1],[800,"Ser Rodrik",200,0],[900,"Hodor",400,0],[700,"Rhargar Targaryen",000,3]]
    wrong=1
    while wrong:
        nm1=int(input("Please enter first character's ID:"))
        idx1=0
        for i in range(9):
            print(i)
            if nm1==list1[i][0]:
                idx1=i
                wrong=0
    check=1
    while check:
        nm2=int(input("Please enter second character's ID:"))
        idx2=0
        for i in range(9):
            if nm2==list1[i][0]:
                idx2=i
                check=0
    print("idx1=",idx1)
    print("idx2=",idx2)
    if list1[idx1][0]==list1[idx2][2]:
        print(list1[idx1][1]," is ",list1[idx2][1],"'s boss!")
    elif list1[idx1][2]==list1[idx2][0]:
        print(list1[idx2][1]," is ",list1[idx1][1],"'s boss!")
    elif list1[idx1][3]==list1[idx2][3]:
        print(list1[idx2][1]," and ",list1[idx1][1]," are same generation!")
    else:
        print(list1[idx2][1]," and ",list1[idx1][1]," are Enemy!")

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#Team_14
if __name__ == '__main__':
    n = int(input("請輸入需要到號碼組數："))
    for i in range(n):
        numLIST = []
        Bingo = []
        x = 1
        while x < 50:
            numLIST.append(x)
            x += 1
        import random
        random.shuffle(numLIST)    
        a = 0
        while a < 6:
            Bingo.append(numLIST[a])
            a += 1  
        print (Bingo)
