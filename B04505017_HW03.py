#!/usr/bin/env python3
# -*- coding:utf-8 -*-

###################################################################
# This is the third program

def odd_of_strings():
    print("Enter a lots of word, prove me,")
    print("and I will pour you out 1s and 0s,")
    strings = input("there shall not be room enough to receive it:")
    longs = len(strings)
    seperated = list(strings)    
    revised = {} 
    
    for i in range(longs):        
        if seperated[i] in revised:
            revised[seperated[i]] = revised[seperated[i]] + 1
        else:
            revised.update({seperated[i]:1})            
            
    #revised = {y:x for x,y in revised.items()}    
    revisedlistoriginal = [(v,k) for k,v in revised.items()]
    
    from operator import itemgetter
    revisedlistoriginal.sort(key=itemgetter(0))    
    revisedlistpercentage_2 = []
    
    for (v, k) in revisedlistoriginal:
        a = round(100*v/longs,3)
        b = k
        revisedlistpercentage_2.append((a,b))     
    #revisedlistpercentage_1 = [(100*v//longs,k) for (k,v) in revisedlistoriginal.items()]    
    
    print("The odds are printed in percentage;that is, %")
    print(revisedlistpercentage_2)
if __name__ == "__main__":
    odd_of_strings()
            