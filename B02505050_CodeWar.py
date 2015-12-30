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
