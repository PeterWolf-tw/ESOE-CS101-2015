#!/usr/bin/env python3
# -*- coding:utf-8 -*-2

#Team01

def jjj(x):
    y=list(x)
    y.append(y[0])
    y.remove(y[0])
    y.append("ay")
    z = ""
    for i in y :
        z = z + i
    return z
if __name__ == '__main__':
    a=input("請輸入一個英文單字")
    print(jjj(a)