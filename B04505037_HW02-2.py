def bin2int(x):
   
    y = int(x)
    z = str(x)
    c = 0 
    r = 10
    k = 0
    u = int(max(str(x)))
    v = (z.find('1'))
      
    if(u>1 or y<0):
        print ('invalid')

    else:
    
        if(v>=1):
         
            while(y>=1):        
                i = y%r
                if (i<=1):
                    c += i*(2**k)
                    k += 1
                    y = y//r
            
                         
        if(v==0):
            while(y>=1):        
                i = y%r
                if (i<=1):
                    c += i*(2**k)
                    k += 1
                    y = y//r        
                    if(len(str(y))<=1):
                        break
              
     
    if(v==0):       
        print (c,"\n") 
    elif(u>1 or y<0):
        print ('\n')
    else:    
        print(-c,"\n")

x = input("Please insert a number: ")
print(bin2int(x))
    