#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#Team01###############
def asiagodtone(yee):
    result = []
    

    for i in range(1,yee+1):
        if yee%i == 0 :
            result.append(i)
            

            
        else:
            continue
    return result

#Team04#####################
def fibonacci(yee):
    fibo = []
    for i in range(0,yee):
        if i == 0 or i == 1 :
            fibo.append(1)
        else:
            fibo.append(fibo[i-1]+fibo[i-2])
    
    return fibo

#Team14########################
def lottery():
    import random
    fuck = []
    result = []
    for i in range(0,49):
        fuck.append(i)
    
    for i in range(0,6):
        srand = random.randint(0,49-i)
        result.append(fuck[srand])
        del fuck[srand]
    result.sort()
    return result
        
if __name__== "__main__":
    t01 = int(input('>>>'))
    print(asiagodtone(t01))
    
    t04 = int(input('>>>'))
    print(fibonacci(t04))
    
    t14 = lottery()
    print(t14)