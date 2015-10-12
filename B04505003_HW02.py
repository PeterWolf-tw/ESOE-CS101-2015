def b2i(c):
   if (c>=0): c=g
   else: c=-g
   
   a = 0
   i = 0
   while g>= 1:
        
      s = g%10
      a = s*(2**i) +a
      i = i+1
      g = g//10
   return a

d = ("djiojoakopaskkadasldkaspkdpaksdpasda:")
c = input(d)
c = int(c)
u = b2i(c)
print(u)
 
    