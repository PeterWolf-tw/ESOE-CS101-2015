#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#team01
def divisorGenerator(n):
    resultlist = []
    
    for i in range(1,n+1):
        if n%i == 0:
            resultlist.append(i)
            
        else:
            continue
    return resultlist

if __name__ == "__main__":
    Ans=divisorGenerator(100)
    print(Ans)
        