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
    
    '''
    Liste = []
    print(Listb)
    for i in Listb:
        Liste.append((i[0],i[1],0))
    print(Liste)
    print(min(Liste))
    Listf = []
    Listg = []
    Listp = []
    L = 0
    O=0
    print("p:",Liste)
    while len(Liste) > 1:
        Listg = []
        Listg.extend(Liste)
        #print(min(Liste))
        
        h = min(Liste)
        B = Liste.index(min(Liste))
        Listf.append(min(Liste))
        Liste.remove(min(Liste))
        A = min(Liste)
        Listf.append(min(Liste))
        Liste.remove(min(Liste))
       
        Max = max(h[2],A[2])
        
        Liste.insert(B,(h[0]+A[0],'00',Max+1))
        #print("e:",Liste)
        #print("g:",Listg)
        
        
        for i in Liste:
            if (Max + 1 - i[2] ) > 1  and O == 0:
                #if (i[2] - Max - 1) > 1 or (i[2] - Max - 1) < -1:
                
                Listp.extend(Listg)
                L = L + 1
                print("p:",Listp)
                Listp = []
                break
        imin=100
        imax=0
        for i in Liste:
            if i[2] > imax:  
                imax = i[2]
            elif i[2] < imin:  
                imin = i[2]
        if imax == imin: 
            Listp.extend(Liste)
            L = L + 1
            print("p:",Listp)
            Listp = []
    Listp.extend(Liste)
    L = L + 1
    print("p:",Listp)
    Listp = []
    
    
    
    '''
    #想試圖做出樹狀圖
    #放棄QQ
    


    return Listb

	
if __name__ == '__main__':
    testSTR01 = "The quick brown fox jumps over the lazy dog"
    result1 = charFreqLister(testSTR01)
    print("result1=",result1)
    testSTR02 = "Jim quickly realized that the beautiful gowns are expensive"
    result2 = charFreqLister(testSTR02)
    print("result2=",result2)