#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#Python Bit Operation

#以大寫 B 和小寫 b 為例：
#先用 ord() 將字符轉為 unicode 編碼序號後，再用 bin() 來看看兩者的二進位碼各為：

print("B:", bin(ord("B")))
print("b:", bin(ord("b")))

#可發現兩者的二進位碼在第 5 位差 1。

print(ord("B")) #"B" 在 Unicode 中的編號
print(ord("b")) #"b" 在 Unicode 中的編號

#將大寫轉為小寫：

print(chr(ord("B") ^ (1 << 5)))
#本來 "B" 的編號應為 66，但藉由上述的 bit operation，將第 5 位 shift 1 位，於是 "B" 的 0b1000010 被轉成了 0b1100010。
#最後我們再用 chr() 來看看 0b1100010 是哪一個字符。

#試試看，如果要把 "b" 轉為大寫，應該怎麼寫？(20 行後有解答)



















#解答
print(chr(ord("b") ^ (1 << 5)))

# 以上全部是為了理解背後的原理。實際操作時，Python 本身已經提供十分方便的 lower() 和 upper() 功能：

#小寫轉大寫
print("this is a book.".upper())
#大寫轉小寫
print("THIS IS A BOOK.".lower())