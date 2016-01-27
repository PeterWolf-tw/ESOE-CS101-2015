#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def buble(yee):
    for i in range(len(yee)-1,0,-1):
        for j in range(0,i):
            if yee[j] > yee[j+1] :
                a = yee[j+1]
                yee[j+1] = yee[j]
                yee[j] = a
    return yee

if __name__== "__main__":
    fuck = [5, 16, 20, 3, 8, 12, 9, 17, 20, 7]
    print(buble(fuck))