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
    
    facLIST = charFreqLister(shit)
    facLEN = len(facLIST)
    freqLISTforcode = []
    charLISTforcode = []
    freqDICTforcode = {}
    for i in facLIST:
        freqLISTforcode.append(i[0])
        charLISTforcode.append(i[1])
        freqDICTforcode[i[1]] = i[0]
    nDICT = {}
    i = 1
    while i < facLEN :
        freqLIST = []
        charLIST = []        
        for h in facLIST:
            freqLIST.append(h[0]) 
            charLIST.append(h[1])  
        n = [charLIST[-2],charLIST[-1]]
        nDICT[i] = n
        f = freqLIST[-2] + freqLIST[-1]
        del freqLIST[-2]
        del freqLIST[-1]
        del charLIST[-2]
        del charLIST[-1]     
        facLIST = []
        for j in range(len(freqLIST)):
            facLIST.append([freqLIST[j],charLIST[j]])
        facLIST.append([f,n])
        facLIST.sort(key= lambda x : x[0] ,reverse=True)
        i += 1
    #print("i=",i," nDICT=",nDICT)
    #print("i=",i," facLIST=",facLIST)    
    resultDICT = {}
    for i in charLISTforcode:
        resultDICT[i] = ""
    for i in range(1,facLEN):
        a = nDICT[i]
        for k in charLISTforcode:
            if k in str(a[0]).replace(", ",","): 
                resultDICT[k] = "1" + resultDICT[k]
            if k in str(a[1]).replace(", ",","):
                resultDICT[k] = "0" + resultDICT[k]
    resultLIST = []
    for i in charLISTforcode:
        if i in resultDICT:
            resultLIST.append([freqDICTforcode[i],i,resultDICT[i]])

    return resultLIST

                                
    

if __name__ == '__main__': 
    
    outputLIST=charFreqLister(input("please enter something:"))   
    print (outputLIST)
    
    output=order(input("please enter something:"))   
    print (output)    
    