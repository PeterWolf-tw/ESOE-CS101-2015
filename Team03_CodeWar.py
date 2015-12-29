#team01
>>> def divisor(n):
	resultLIST=[]
	for i in range(1,n+1):
		if n%i==0:
			resultLIST.append(i)
		    return resultLIST
			
>>> #team04
>>> def feynman(n):
	number=0
	a=1
	b=1
	if n>2:
		a=b
		b=a+b
		n=n-1
		number=b
		return number
	else:
		number=b
		return number
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

#team 12
S2V = {'0': 0,
         '1': 1,
         '2': 2,
         '3': 3,
         '4': 4,
         '5': 5,
         '6': 6,
         '7': 7,
         '8': 8,
         '9': 9,
         'A': 10,
         'B': 11,
         'C': 12,
         'D': 13,
         'E': 14,
         'F': 15,
         'G': 16,
         'H': 17,
         'I': 18,
         'J': 19,
         'K': 20,
         'L': 21,
         'M': 22,
         'N': 23,
         'O': 24,
         'P': 25,
         'Q': 26,
         'R': 27,
         'S': 28,
         'T': 29,
         'U': 30,
         'V': 31,
         'W': 32,
         'X': 33,
         'Y': 34,
         'Z': 35,
         'a': 36,
         'b': 37,
         'c': 38,
         'd': 39,
         'e': 40,
         'f': 41,
         'g': 42,
         'h': 43,
         'i': 44,
         'j': 45,
         'k': 46,
         'l': 47,
         'm': 48,
         'n': 49,
         'o': 50,
         'p': 51,
         'q': 52,
         'r': 53,
         's': 54,
         't': 55,
         'u': 56,
         'v': 57,
         'w': 58,
         'x': 59,
         'y': 60,
         'z': 61}

def m2n():

    x = input("Please enter a number:")
    m = int(input("Please enter the initial base:"))
    n = int(input("Please enter the final base:"))

    integer = 0
    for character in x:
        assert character in S2V, "Unknown character!"
        value = S2V[character]
        assert value < m , "Digit outside base!"
        integer *= m
        integer += value

    V2S = dict(map(reversed, S2V.items()))

    array = []
    while integer !=0:
        value = integer % n
        integer //= n
        array.append(V2S[value])

    ans = "".join(reversed(array))

    print (ans)

m2n()
#team 14
>>> def lottery(n):
	import random
	k=0
	yee=[]
	times=int(n)
        if k<times:
               number=random.int(1,49)
               yee.append(number)
               k+=1
               return yee
	else:
                print(yee)

	
