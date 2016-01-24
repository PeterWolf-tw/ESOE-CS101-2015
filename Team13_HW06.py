#!/usr/bin/env python 3
#-*- coding:utf-8 -*-

#程式開始前，在檔頭和程式內文之間至少空一行
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


#請務必使用程式進入點，並做出相應合適的縮排。
#if __name__ == '__main__':
sortList = [5, 16, 20, 3, 8, 12, 9, 17, 20, 7]
selectionSort(sortList)
print(sortList)