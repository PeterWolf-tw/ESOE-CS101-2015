#!/usr/bin/env python3
# -*- coding:utf-8 -*-




def charFreqLister(inputSTR):
    resultLIST = []
    


    
    for x in inputSTR:
        c = inputSTR.count(x)
        if (x,c/len(inputSTR)) not in resultLIST:
            resultLIST.append((x,c/len(inputSTR)))
    resultLIST.sort( key = lambda x : x[1], reverse=True)
        
    return resultLIST

        

              
               

if __name__ == "__main__":
    output = charFreqLister(input("give me something shit:"))    
    print(output)



        