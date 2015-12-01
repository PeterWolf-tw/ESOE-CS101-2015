#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def jeremy(x):
    bitchLIST = []
    yeeSTR = x
    curry=len(x)
    floatcurry=float(curry)
    for i in yeeSTR:
        bitchLIST.append((i,float(yeeSTR.count(i))/floatcurry))#計算機率
    fuckingset=set(bitchLIST)#用set把重複的刪掉
    bitchLIST=list(fuckingset)#調回list才能用sorted來排列大小
    bitchLIST=sorted(bitchLIST,key=lambda a:a[1],reverse=True)#排列
    return bitchLIST
    
    
    
   
if __name__== "__main__":
    x=input()
    
    print(jeremy(x))
      