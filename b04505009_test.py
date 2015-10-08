#!/usr/bin/env python 3
#-*- coding:utf-8 -*-

def int2bin(N):
    '''
    本函式將 int 整數轉為 bin 二進位制表示
    '''
    tmplist = list(binNumber)
    tmplist = [int(i) for i in tmplist]
    print (tmplist)
    a = len (tmplist) - 1
    b = 0
    s = 0
    if tmplist[0] == 0:
        while a >= 0:
        
            x = tmplist[a]
            s = s + (x*(2**b))
            a -= 1
            b += 1             
        print("{0} 的十進位表示為 {1}.".format(binNumber, s))
    else:
        while a >= 0:
            
            x = (tmplist[a] + 1) % 2
            s = s + (x*(2**b))
            a -= 1
            b += 1             
        print("{0} 的十進位表示為 {1}.".format(binNumber, -s-1))            
        

    return None

if __name__ == '__main__':
    binNumber = "01100100"
    
    int2bin(binNumber)
    

