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
            b *= 2
        print("{0} 的十進位表示為 {1}.".format(binNumber, -s-1))

    return None

if __name__ == '__main__':
    binNumber = "01100100"

    bin2int(binNumber)
    #這個 function 處理正負數時有問題。請改進。e.g., "100" 的十進位表示應為 4 而不是 -4。

    p2_19a = 10
    p2_19b = 17
    p2_19c = 6
    p2_19d = 8

    p2_20a = 14
    p2_20b = 8
    p2_20c = 13
    p2_20d = 4

    p2_22a = "00010001 11101010 00100010 00001110"
    p2_22b = "00001110 00111000 11101010 00111000"
    p2_22c = "01101110 00001110 00111000 01001110"
    p2_22d = "00011000 00111000 00001101 00001011"

    p3_28a = 234
    p3_28b = 560
    p3_28c = 874
    p3_28d = 888

    p3_30a = 234
    p3_30b = 560
    p3_30c = 875
    p3_30d = 889



