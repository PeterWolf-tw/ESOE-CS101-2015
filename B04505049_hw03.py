#!/usr/bin/env python3
# -*- coding:utf-8 -*

def charfreqlister(inputSTR):
    resultLIST = []
    
    

for a in inputSTR:
   A = inputSTR.count(a)
   B =  len(inputSTR)
   if (a,A/B) not in resultLIST:
       resultLIST.append(i,A/B)
    resultLIST.sort( key = lambda x : x[1])
      return resultLIST
    
       
    
    



if __name__== "__main__":
    print(charFreqLister(input("please enter simething:")))
