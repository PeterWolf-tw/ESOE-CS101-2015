#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Team01
def CommonDivisor(n):
    for i in range(1,n+1):
        if n%i == 0:
            print(i)
    return None
if __name__ == "__main__":
    n=input("Please input a number:")
    CommonDivisor(int(n,10))