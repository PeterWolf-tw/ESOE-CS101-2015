#!/usr/bin/env python3
# -*- coding:utf-8 -*-

alist=[]
orig=input("type a sentence here:")
def list2freqdict(result):
    
    blist=[orig]
    n=len(orig)
    for k in orig:
        c=orig.count(k)
        if (k,c/n)not in alist:
            item=k,c/n
            alist.append(item)
            alist.sort(key = lambda x : x[1], reverse=True)
        else:
            pass
    result=alist
    return result

if __name__ == "__main__":  
    result=alist
    print(list2freqdict(result))
