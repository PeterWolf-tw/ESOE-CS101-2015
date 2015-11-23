#!/usr/bin/env python3
# -*- coding:utf-8 -*-




def charFreqLister(inputSTR):
    resultLIST = []
    freq = []


    
    for i in inputSTR:
        c = inputSTR.count(i)
        if (i,c/len(inputSTR)) not in resultLIST:
            resultLIST.append((i,c/len(inputSTR)))
    resultLIST.sort( key = lambda x : x[1], reverse=True)
        
    return resultLIST

        

              
               

if __name__== "__main__":
    fuck = "asia god tone gg3be0"
    shit = charFreqLister(fuck)
    print(shit)


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
        