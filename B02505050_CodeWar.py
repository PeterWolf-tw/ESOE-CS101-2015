#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#team01
def e(x):
    a = []
    for i in range(1,x+1):
        if x%i == 0:
            a.append(i)
    return a
if __name__ == '__main__':
    d=int(input("in put a number:") ) 
    print(e(d))
    
    
