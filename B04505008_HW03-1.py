# !/usr/bin/env python3
#  -*- coding:utf-8 -*-

def charFreqLister(inputSTR):

    n = len(inputSTR)
    resultLIST = []

    for i in inputSTR:
        j = float('%.3f'%(str(inputSTR).count(i)/n))
        if (j,i) not in resultLIST:
            resultLIST.append((j,i))
    resultLIST = list(resultLIST)
    resultLIST.sort(reverse=True)
    return resultLIST

def order(shit):
    
    n=len(shit)
    resultLIST=[]
    
    for a in shit:
        A = shit.count(a)/n
        codea = []
        if (A,a,codea) not in resultLIST:
            resultLIST.append((A,a,codea))
    resultLIST.sort(reverse=False)
    
    for(A,a,codea) in resultLIST:
        for(B,b,codeb) in resultLIST:
            for(C,c,codec) in resultLIST:
                if A <= B <= C <1:
                    K=A+B
                    codea.append("0")
                    codeb.append("1")
                    resultLIST.append((K,"ghost","ghostcode"))
            
    

if __name__ == '__main__': 
    
    outputLIST=charFreqLister(input("please enter something:"))
       
    out123=order(outputLIST)    
    print (out123)