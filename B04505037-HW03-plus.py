# !/usr/bin/env python3
#  -*- coding:utf-8 -*-

#試了很久都出現錯誤 去查了稍微看得懂的程式來修還是弄不出來

import heapq

def encode(inputLIST):
    
    n = len(inputLIST)
    resultLIST = []
    
    for i in inputLIST:
        j = inputLIST.count(i)/n
        resultLIST.append(([j,i,[""]]))
    #resultLIST = list(set(result))
    resultLIST.sort(key=lambda tup: tup[0], reverse=True)
    #return resultLIST    
    tree = resultLIST
    heapq.heapify(tree)
    
    while len(tree)>1:
        left, right = sorted([heapq.heappop(tree), heapq.heappop(tree)], key=len)
        for item in left[2]:
            item = '0' + item
        for item in right[2]:
            item = '1' + item
        tree.append(([left[0:1]+right[0:1],left[2]+right[2]]))
        #heapq.heappush(tree, [left[0:1]+right[0:1]] + left[2] + right[2])])
    return sorted(heapq.heappop(tree)[1:], key=lambda p: (len(p[-1]), p))
    
inputLIST = input("Please insert something: ")

print(encode(inputLIST))



#做一點修改然後跟HW03結合的程式(可以做出來)
'''
def charFreqLister(inputLIST):

    
    n = len(inputLIST)
    result = []

    for i in inputLIST:
        j = inputLIST.count(i)/n
        result.append((i,j))
    resultLIST = list(set(result))
    resultLIST.sort(key=lambda tup: tup[1], reverse=True)
    return resultLIST    
    tree = [[j, [i, ""]] for i, j in resultLIST]

    heapq.heapify(tree)
    while len(tree)>1:

        left, right = sorted([heapq.heappop(tree), heapq.heappop(tree)], key=len)

        for pair in left[1:]:
            pair[1] = '1' + pair[1]
        for pair in right[1:]:
            pair[1] = '0' + pair[1]

        heapq.heappush(tree, [left[0]+right[0]] + left[1:] + right[1:])
    return sorted(heapq.heappop(tree)[1:], key=lambda p: (len(p[-1]), p))
'''