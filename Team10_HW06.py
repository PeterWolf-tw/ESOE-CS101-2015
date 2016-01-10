#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#請參考 http://interactivepython.org/runestone/static/pythonds/SortSearch/sorting.html
#中提供的 bubble sorting 演算法，將整數列表 [5, 16, 20, 3, 8, 12, 9, 17, 20, 7] 由大排到小。






def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [5, 16, 20, 3, 8, 12, 9, 17, 20, 7]
bubbleSort(alist)
print(alist)
