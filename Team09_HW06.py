#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#請參考 http://interactivepython.org/runestone/static/pythonds/SortSearch/sorting.html
#中提供的 bubble sorting 演算法，將整數列表 [5, 16, 20, 3, 8, 12, 9, 17, 20, 7] 由大排到小。

def bubble():
    x = []
    x = input("give me some numbers:").split(",")
    x[:] = [int(a) for a in x]
    l = len(x)
    for k in range (0 , l-1 ):
        n = 0
        for i in range (l-1, k, -1):
            b = x[i]
            c = x[i-1]
            if b < c:
                del x[i]
                del x[i-1]
                x.insert(i-1, b)
                x.insert(i, c)
            else:
                continue
    print (x)
        
            


if __name__ == "__main__":
    print(bubble())