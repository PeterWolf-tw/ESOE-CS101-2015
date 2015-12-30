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
    
#team02
def Pig(word):
    fixword = word.isalpha()   
    if fixword == True:
        x = word[0]
        y = len(word)
        word1 = word[1:y]
        word1 = word1 + x + 'ay'
        return word1
    else:
        return ('invalid word')
 
word = input('Please enter an English word: ')
print(Pig(word))






#team04
def term():
    n = int(input("what is the number of term?"))
    if n < 1:
        t = [0,1,1]
    for i in range(n+1):
        if i > 2:
            t.append(t[i-2]+t[i-1])
    if n >= 0:
        print(t[n])
