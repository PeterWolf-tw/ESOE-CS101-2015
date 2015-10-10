#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def bit_dex(x):
    i = 0
    d = 0
    while x>=1:
        c = x%10
        d = c*(2 ** i) + d
        i = i + 1
        x = x//10
    return d
a = ("What number do you want to convert? Come and enter it. It is:")
x = input(a)
x = int(x)
e = bit_dex(x)
print(e)

'''

2-19
a. 10
b. 17
c. 6
d. 8

2-20

a. 14
b. 8
c. 13
d. 4

2-22
a. 00010001 11101010 00100010 00001110
b. 00001110 00111000 11101010 00111000
c. 01101110 00001110 00111000 01001110
d. 00011000 00111000 00001101 00001011

3-28
a. 234
b. 560
c. 874
d. 888

3-30
a. 234
b. 560
c. 875
d. 889
'''


