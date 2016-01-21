#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def bubble(x):    
    y = len(x)
    z = list(x)
    for i in range(0,y):
        #print(z)
        x.reverse()
        x.remove(max(z))
        x.reverse()
        x.insert(i,max(z))
        z.remove(max(z))
    return x
    
if __name__== "__main__":
    x = [5, 16, 20, 3, 8, 12, 9, 17, 20, 7]
    print(x[1])
    print(max(x))    
    print(bubble(x))
