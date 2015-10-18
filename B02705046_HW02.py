#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#Python 程式的前兩行是固定的，請牢記。


def bin2int(N):
    n = str(N)
    an = 0
    p = 0
    while p < len(n):
        if n[p] == '1':
            an += 2 ** (len(n) - 1 - p)
        p += 1
    return an

if __name__ == '__main__':
    #下次加個程式的進入點吧！

    binNumber = 1010
    print(bin2int(binNumber))
#P2-19
#a. 10bits
#b. 17bits
#c. 6bits
#d. 8bits
#P2-20
#a. 14digits
#b. 8digits
#c. 13digits
#d. 4digits
#P2-22
#a. 00010001 11101010 00100010 00001110
#b. 00001110 00111000 11101010 00111000
#c. 01101110 00001110 00111000 01001110
#d. 00011000 00111000 00001101 00001011

#P3-28
#a. 280 #錯
#b. 682 #錯
#c. 741 #錯
#d. 756 #錯
#請務必再讀一次 complement (補數) 的章節
#P3-30
#a. 234
#b. 560
#c. 875
#d. 889
