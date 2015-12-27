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
    Ans01=divisorGenerator(100)
    print(Ans01)
    
    
    
#team02
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def piglatintranslator(enter_a_word):

    letterlist=[]

    if len(enter_a_word)>1:
        letterlist = list(enter_a_word)
    else:
        print("valid word! Dumbo!")
    print("".join(letterlist[1:]) + letterlist[0] + "ay")
    return letterlist




if __name__ == "__main__": 
    piglatintranslator("test")
    
    
#team03


#team04
def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

if __name__ == "__main__":
    print (fib(6))