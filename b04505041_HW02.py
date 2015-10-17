#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#Python 程式的前兩行是固定的，請牢記。

def int2bin(N):
    tmpLIST = []
    while N > 0:
        remainder = int(N % 2)
        tmpLIST.append(remainder)
        N = (N - remainder) / 2
    tmpLIST.append(0)

    ans = ""
    for j in tmpLIST[::-1]:
        ans = ans + str(j)
    print("{0} 的二進位表示為 {1}.".format(N, ans))
    return None

#你的程式內容是空的。

#助教我真的沒有任何想法啊！！！
#先放我一馬吧還是能再補交～
#請多參考同學的解法，和同組同學討論。可以補交，但我不會放水。(Peter.w)


#P2.19
    a.10
    b.17
    c.6
    d.8
#P2.20
    a.14
    b.8
    c.13
    d.4
#P2.22
    a.00010001 11101010 00100010 00001110
    b.00001110 00111000 11101010 00111000
    c.01101110 00001110 00111000 01001110
    d.00011000 00111000 00001101 00001011
#P3.28
    a.234
    b.overflow #錯
    c.874
    d.888
#P3.30
    a.234
    b.overflow #錯
    c.875
    d.889