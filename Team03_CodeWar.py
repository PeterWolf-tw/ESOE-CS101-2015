#Team09
import os
import random

def play1():
    play2()


def play2():
    ans=[]
    t=0
    while t<4:
        num = str(random.randrange(10))
        if num not in ans:
            ans.append(num)
            t+=1

    #print (ans) #answer
          
    while True:
        print ("Guess a 4 digit number without repetition:")
        A=0
        B=0
        input1=input()
        
        
        try:
            int(input1)
            
            if "".join(str(n) for n in ans) == input1:
                print ("4,A,0,B")
                print ("Congratulation☺, press anything to continue.\n")
                os.system('pause')
                play1()
            elif len(input1) != 4:
                print ("Error\n")
            
            else:
                for n in range(4):
                    if input1[n] == ans[n]:
                        A+=1
                    if input1[n] in ans:
                        B+=1
                    
                print ("%d,A,%d,B" % (A, B-A))
        except:
            print ("Error\n")

play1()
