
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def charFreqLister(inputSTR):
    resultLIST = []
    while len(inputSTR) > 0:
        n = 0
        letterLEN = inputSTR.count(inputSTR[n])
        letterFREQ = 1.0*letterLEN/len(inputSTR)
        resultLIST.append((inputSTR[n],letterFREQ))   
        inputSTR = inputSTR.strip(inputSTR[n])
        n += 1
    return resultLIST

if __name__ == "__main__":
    a = "My name is Alex, Hello my friend!"
    print(charFreqLister(a))
