#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def charFreqLister(b):
    Lista = []    
    Listb = []
    Listc = []
    Listd = []
    for i in b:
        Lista.append(i)
        #print(Lista.count(i))
        d = Lista.count(i)/len(b)
        Listc.append(d)
    a = 0
    for i in b:
        c = (Listc[a],i)
        Listb.append(c)
        a = a + 1

    #print(Listb)
    #print(Listb[2][1])
    e = 0
    f = 0

    Listb.sort()
    #print(Listb)
    #print(Listb)
    Listd.extend(Listb)
    #print("lalalala")
    #print(Listd)
    for i in Listd:
        for j in Listd:
            if i != j:
                if i[1] == j[1]:
                    if i[0] < j[0]:
                        Listb[e] = (10,10)                       
                    else:
                        Listb[f] = (10,10)                     
            f = f + 1
        e = e + 1
        f = 0
    #print(Listb)
    g = len(Listb)
    for i in range(g):
        #print("yaya",i)
        if Listb[g-i-1][0] == 10:
            del Listb[g-i-1]
            #print("hahahaha",Listb)
    #print(Listb)

    Listb.reverse()
    #print(Listb)


    return Listb


if __name__ == '__main__':
    testSTR01 = "The quick brown fox jumps over the lazy dog"
    result1 = charFreqLister(testSTR01)
    print("result1=",result1)
    testSTR02 = "Jim quickly realized that the beautiful gowns are expensive"
    result2 = charFreqLister(testSTR02)
    print("result2=",result2)
