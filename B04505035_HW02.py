x=("a binary like   ")
cin=str(input(x))
j=len(cin)-1
sum=0
k=0
while j>=0:
   
    sum+=int(cin[k])*2**j
    
    j=j-1
    k=k+1




print(sum)



#P2-19
#a. 10bits
#b. 17bits
#c. 6bits
#d. 8bits
#P2-20
#a. 14digits
#b. 8digits
#c. 13digits
#d. 4digits
#P2-22
#a. 00010001 11101010 00100010 00001110
#b. 00001110 00111000 11101010 00111000
#c. 01101110 00001110 00111000 01001110
#d. 00011000 00111000 00001101 00001011
#P3-28
#a. 280
#b. 682
#c. 764
#d. 756
#P3-30
#a. 234
#b. 560
#c. 875
