#!/usr/bin/env python 3
#-*- coding:utf-8 -*-
    
def bin2int(N):
    '''
    本函式將 bin 二進位制表示數轉為 int 整數
    '''
    mod = 0
    x = 0
    i = 0
    a = 0
    while N > 0: 
        mod = int(N % 10)
        b = 2 ** i
        a =  a + mod*b
        i = i + 1
        N = (N - mod) / 10 

    print("{0} 的十進位表示為 {1}.".format(binNumber, a))
if __name__ == '__main__':
    binNumber = 1100100 #"01100100"
        
    bin2int(binNumber)    
    

