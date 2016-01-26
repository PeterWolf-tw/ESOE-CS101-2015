#!/usr/bin/env python
# -*- coding: utf-8 -*-


def bubble(List):
    for j in range(len(List)-1,0,-1):
        for i in range(0,j):
            if List[i]>List[i+1]:List[i],List[i+1]=List[i+1],List[i]
    return List

# 請務必記得加上程式進入點 if __name__ == '__main__':
testlist = [5, 16, 20, 3, 8, 12, 9, 17, 20, 7]
print('final:', bubble(testlist))