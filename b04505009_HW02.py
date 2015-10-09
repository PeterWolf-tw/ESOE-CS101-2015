#!/usr/bin/env python 3
#-*- coding:utf-8 -*-

def bin2int(N):
    '''
    本函式將 bin 整數轉為 int 十進位制表示
    '''
    binNumberlist = list(binNumber) 
    binNumberlist = [int(i) for i in binNumberlist]
    print (binNumberlist)
    a = len (binNumberlist) - 1 
    b = 1 
    s = 0
    if binNumberlist[0] == 0:
        while a >= 0:
            x = binNumberlist[a]
            s = s + (x * b)
            a -= 1
            b *= 2             
        print("{0} 的十進位表示為 {1}.".format(binNumber, s))
    else:
        while a >= 0: 
            x = (binNumberlist[a] + 1) % 2 
            s = s + (x * b)
            a -= 1
            b *= 1             
        print("{0} 的十進位表示為 {1}.".format(binNumber, -s-1))           
        
    return None

if __name__ == '__main__':
    binNumber = "01100100"
    
    bin2int(binNumber)
    
    
    

