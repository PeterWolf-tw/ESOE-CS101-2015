#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#Python 程式的前兩行是固定的，請牢記。
#另，建議你使用一個 IDE。你的中文字符在我這裡看起來都像是亂碼。

#�Ĥ@�D�O���O�o�˥����A�|���H�Ф@�U�Aby jeffntu
if __name__ == '__main__':
    n = 0
    #p = raw_input('input a bin number:\n')
    p = input('input a bin number:\n')
    #raw_input() 是 Python2 的函式。從 Python3 開始都用 input()
    for i in range(len(p)):
        n = n * 2 + ord(p[i]) - ord('0')
    #print n
    print(n)
    #print n 是 Python2 的語法。從 Python3 開始都用 print(n)








#2-19   a.10  b.17  c.6  d.8
#2-20   a.14  b.8  c.13  d.4
#2-22   a. 00010001  11101010  00100010  00001110  b. 00001110  00111000  11101010  00111000  c.01101110  00001110  00111000  01001110  d.00011000  00111000  00001101  00001011
#3-28   a.234  b.560  c.874  d.888
#3-30   a.234  b.560  c.875  d.889