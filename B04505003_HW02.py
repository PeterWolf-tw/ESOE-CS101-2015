def b2i(c):
   if c>=0:
      g=c
   else: 
      g=-c
   
   a = 0
   i = 0
   while g>= 1:
        
      s = g%10
      a = s*(2**i) +a
      i = i+1
      g = g//10
   return a

d = ("Please enter a binary number:")
c = input(d)
c = int(c)
if c>=0:
 u = b2i(c)
else:
   u=-b2i(c)

print("The decimal number of" ,c,"is",u)





#2-19
# a 10
# b 17
# c 6
# d 8
#2-20
# a 14
# b 8
# c 13
# d 4
#2-22
# a 00001001 11101010 00100010 00001110
# b 00001110 00111000 11101010 00111000
# c 01101110 00001110 00111000 01001110
# d 00011000 00111000 00001101 00001011
#3-28
# a 765
# b 439
# c-874
# d-888
#3-30
# a 766
# b 440
# c-875
# d-889
