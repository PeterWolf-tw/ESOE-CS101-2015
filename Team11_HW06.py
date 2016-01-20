#!/usr/bin/env python3
#-*- coding:utf-8 -*-
def BubbleSort(LIST):
    for j in range(len(LIST)-1,0,-1):
        for i in range(j):
            if LIST[i] < LIST[i+1]:
                n = LIST[i]
                LIST[i] = LIST[i+1]
                LIST[i+1] = n


if __name__ == '__main__': 
    LIST = [5, 16, 20, 3, 8, 12, 9, 17, 20, 7]
    BubbleSort(LIST)
    print(LIST)