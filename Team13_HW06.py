#!/usr/bin/env python 3
#-*- coding:utf-8 -*-
#bubble sort descending
def selectionSort(sortList):
    for i in range(len(sortList)-1,0,-1):
        positionOfMin=0
        for j in range(1,i+1):
            if sortList[j]<sortList[positionOfMin]:
                positionOfMin = j

        temp = sortList[i]
        sortList[i] = sortList[positionOfMin]
        sortList[positionOfMin] = temp

sortList = [5, 16, 20, 3, 8, 12, 9, 17, 20, 7]
selectionSort(sortList)
print(sortList)
