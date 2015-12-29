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
    
    
    
    
    
    
    
    
    
    
    
    #!/usr/bin/env python3
    # -*- coding:utf-8 -*-
    for i in range(0,9):
        for c in range(0,9):
            print (i*c,end="\n")    