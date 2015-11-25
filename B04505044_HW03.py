#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def charFreqLister(STR):
    LIST = []
    
    
    for i in STR:
        x = STR.count(i)
        if (float('%.3f'%(x/len(STR))),i) not in LIST:
            LIST.append((float('%.3f'%(x/len(STR))),i))
    LIST.sort(reverse=True)

    return LIST

if __name__== "__main__":
    output= charFreqLister(input("give me something shit:"))
    print(output)
