#######################################
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# encoding: utf-8

#作業 1


def bin2int(N):    
    Sum = 0
    L = len(str(N))
    STR = str(N)    
    a=0
    
    while L > 0:        
        n = int(STR[a])*(2**int(L-1))
        L = L - 1
        a = a + 1
        Sum = Sum + n
    return Sum

if __name__ == '__main__':
    x = 111000
    ans = bin2int(x)
    
    print("{0} 的十進位表示為 {1}.".format(x, ans))
    
###########################################
#作業 2. 課本 Ch2. P2.19 a.=10
#作業 2. 課本 Ch2. P2.19 b.=17
#作業 2. 課本 Ch2. P2.19 c.=6
#作業 2. 課本 Ch2. P2.19 d.=8
##########################################
#作業 3. 課本 Ch2. P2.20 a.=14
#作業 3. 課本 Ch2. P2.20 b.=8
#作業 3. 課本 Ch2. P2.20 c.=13
#作業 3. 課本 Ch2. P2.20 d.=4
############################################
#作業 4. 課本 Ch2. P2.22 a.=00010001 11101010 00100010 00001110
#作業 4. 課本 Ch2. P2.22 b.=00001110 00111000 11101010 00111000 
#作業 4. 課本 Ch2. P2.22 c.=01101110 00001110 00111000 01001110
#作業 4. 課本 Ch2. P2.22 d.=00011000 00111000 00001101 00001011
############################################
#作業 5. 課本 Ch3. P3.28 a.=234
#作業 5. 課本 Ch3. P3.28 b.=560
#作業 5. 課本 Ch3. P3.28 c.=874
#作業 5. 課本 Ch3. P3.28 d.=888
##############################################
#作業 6. 課本 Ch3. P3.30 a.=234
#作業 6. 課本 Ch3. P3.30 b.=560
#作業 6. 課本 Ch3. P3.30 c.=875
#作業 6. 課本 Ch3. P3.30 d.=889


        
    
