#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def BubbleSort1(inputlist):
    length = len(inputlist) - 1
    n = 0
    while n < len(inputlist):
        for i in range(0,length):
            if inputlist[length - i - 1] < inputlist[length - i]:
                x = inputlist[length - i]
                inputlist[length - i] = inputlist[length - i - 1]
                inputlist[length - i - 1] = x
                n = 0
            else:
                n = n + 1
    return (inputlist)


def BubbleSort2(inputlist):
    for i in range(len(inputlist)-1,0,-1):
        for j in range(i):
            if inputlist[j]<inputlist[j+1]:
                x = inputlist[j]
                inputlist[j] = inputlist[j+1]
                inputlist[j+1] = x
    return (inputlist)


if __name__ == '__main__':
    list = [5, 16, 20, 3, 8, 12, 9, 17, 20, 7]
    print(BubbleSort1(list))
    print(BubbleSort2(list))

    