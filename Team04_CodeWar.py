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