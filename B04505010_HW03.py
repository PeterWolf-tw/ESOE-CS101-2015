#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#無法執行底線"_",逗號","括號"()"



def charFreqLister(inputSTR):
    resultLIST = []
    


    
    for i in inputSTR:
        c = inputSTR.count(i)
        if (i,c/len(inputSTR)) not in resultLIST:
            resultLIST.append((i,c/len(inputSTR)))
    resultLIST.sort( key = lambda x : x[1])
        
    return resultLIST


    

def huffmanTranslater(inputSTR):
    resultLIST = []
    yee = []
    char = []
    char2 = []
    freq = []
    freq2 = []
    tree =[]
    ahq = []
    huf = []
    k = 0
    m = 0
    
    
    for i in inputSTR:
        c = inputSTR.count(i)
        if (i,c/len(inputSTR)) not in yee:
            yee.append((i,c/len(inputSTR)))
    yee.sort( key = lambda x : x[1])    
    for i in yee:
        freq.append(i[1])
        freq2.append(i[1])
        if i[0] == " ":
            char.append("_")
            char2.append("_")
            ahq.append("_")
        else :
            char.append(i[0])
            char2.append(i[0])
            ahq.append(i[0])
        #tree.append(i)
        huf.append("")
        k = k+1
        m = m+1
    
    while(freq[0] != 1):
        yee2 = []
        j = 0
        if freq[0] == freq[1]:
            freq[1]=freq[0]+freq[1]
            if len(char[1]) > len(char[0]):
                char[1]=(char[1],char[0])
            else :
                char[1]=(char[0],char[1])
        else :
            freq[1]=freq[0]+freq[1]
            char[1]=(char[0],char[1])
        del freq[0]
        del char[0]
        for i in char:
            yee2.append((i,freq[j]))
            j = j+1
            k = k+1
        yee2.sort( key = lambda x : x[1])
        freq = []
        char = []
        for i in yee2:
            freq.append(i[1])
            char.append(i[0])
            ahq.append(i[0])
            tree.append(i)
            
    
    for i in range(0,m-1):
        temp = []
        temp2 = []
        for j in range(k-1,k-i-2,-1):
            temp.append(ahq[j])
        k = k-i-1
        for j in range(k-1,k-i-3,-1):
            temp2.append(ahq[j])
        for j in temp:
            if j not in temp2:
                a = str(j[0])
                for ii in range(0,m):
                    if char2[ii] in a :
                        huf[ii] +="0"
                a = str(j[1])
                for ii in range(0,m):
                    if char2[ii] in a :
                        huf[ii] +="1"
    r = zip(freq2,char2,huf)
    for i in r:
        resultLIST.append(i)

               

    return resultLIST    
    
              

if __name__== "__main__":
    fuck = "asia god tone"
    shit = charFreqLister(fuck)
    test = huffmanTranslater(fuck)
    print(shit)
    print(test)


#░░░░░░░░░░░░░░░░░░░░░░░░░░
#░░░░░░░░░░░░░▄███▄▄▄░░░░░░
#░░░░░░░░░▄▄▄██▀▀▀▀███▄░░░░
#░░░░░░░▄▀▀░░░░░░░░░░░▀█░░░
#░░░░▄▄▀░░░░░░░░░░░░░░░▀█░░                   ░     ░         ░░░░░         ░░░░░░
#░░░█░░░░░▀▄░░▄▀░░░░░░░░█░░                    ░   ░          ░             ░
#░░░▐██▄░░▀▄▀▀▄▀░░▄██▀░▐▌░░                      ░            ░░░░          ░░░░░
#░░░█▀█░▀░░░▀▀░░░▀░█▀░░▐▌░░                      ░            ░             ░
#░░░█░░▀▐░░░░░░░░▌▀░░░░░█░░                      ░            ░░░░░         ░░░░░░
#░░░█░░░░░░░░░░░░░░░░░░░█░░          
#░░░░█░░▀▄░░░░▄▀░░░░░░░░█░░
#░░░░█░░░░░░░░░░░▄▄░░░░█░░░ 
#░░░░░█▀██▀▀▀▀██▀░░░░░░█░░░
#░░░░░█░░▀████▀░░░░░░░█░░░░
#░░░░░░█░░░░░░░░░░░░▄█░░░░░
#░░░░░░░██░░░░░█▄▄▀▀░█░░░░░
#░░░░░░░░▀▀█▀▀▀▀░░░░░░█░░░░
#░░░░░░░░░█░░░░░░░░░░░░█░░░
        