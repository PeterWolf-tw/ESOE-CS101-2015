#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#請參考 http://interactivepython.org/runestone/static/pythonds/SortSearch/sorting.html
#中提供的 bubble sorting 演算法，將整數列表 [5, 16, 20, 3, 8, 12, 9, 17, 20, 7] 由大排到小。

def bubble(a):    
    b = len(a)
    c = list(a)
    for i in range(0,b):
        #print(c)
        a.reverse()
        a.remove(max(c))
        a.reverse()
        a.insert(i,max(c))
        c.remove(max(c))
    return a
        
    


if __name__== "__main__":
    a = [5, 16, 20, 3, 8, 12, 9, 17, 20, 7]
    print(a[1])
    print(max(a))    
    print(bubble(a))