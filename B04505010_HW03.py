#!/usr/bin/env python3
# -*- coding:utf-8 -*-




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
    freq = []
    tree =[]
    
    for i in inputSTR:
        c = inputSTR.count(i)
        if (i,c/len(inputSTR)) not in yee:
            yee.append((i,c/len(inputSTR)))
    yee.sort( key = lambda x : x[1])    
    for i in yee:
        freq.append(i[1])
        char.append(i[0])
        tree.append(i)
    
    while(freq[0] != 1):
        yee2 = []
        j = 0
        freq[1]=freq[0]+freq[1]
        del freq[0]
        del char[0]
        for i in char:
            yee2.append((i,freq[j]))
            j = j+1
        yee2.sort( key = lambda x : x[1])
        freq = []
        char = []
        for i in yee2:
            freq.append(i[1])
            char.append(i[0])
            tree.append(i)
            
    return tree    
    
              

if __name__== "__main__":
    fuck = "aaaabbbccd"
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
        