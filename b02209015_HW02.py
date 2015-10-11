#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#    '''
 #   本函式將 int 整數轉為 bin 二進位制表示
  #  '''
   # tmpLIST = []
    #while N > 0:
     #   remainder = int(N % 2)
      #  tmpLIST.append(remainder)
       # N = (N - remainder) / 2
    #tmpLIST.append(0)

    #ans = ""
    #for j in tmpLIST[::-1]: #將 tmpLIST 中的數字從尾至頭傳入 j
     #   ans = ans + str(j)
    #print("{0} 的二進位表示為 {1}.".format(N, ans))
    #return None


#作業 1.
# 請參考上例，自己寫一個將二進位表示數轉為十進位制的函式：


#def bin2int(N):
 #   '''
  #  本函式將 bin 二進位制表示數轉為 int 整數
   # '''

    #return None


#if __name__ == '__main__':
 #   intNumber = 100
  #  int2bin(intNumber)

   # binNumber = "01100101"
    #bin2int(number)
    
print("Enter a binary number:")
i = 0
dec = 0
n = input()
while(n > 0):
 rem = n % 10
 if rem == 1:
 n /= 10
 i += 1
 dec = dec + rem*(2**i)
print("The decimal number is:", dec)

#作業 2. 課本 Ch2. P2.19
    #a. 10
    #b. 17
    #c. 6
    #d. 8
    
#作業 3. 課本 Ch2. P2.20
    #a. 14
    #b. 8
    #c. 13
    #d. 4
    
#作業 4. 課本 Ch2. P2.22
    #a. 00010001 11101010 00100010 00001110
    #b. 00001110 00111000 11101010 00111000
    #c. 01101110 00001110 00111000 01001110
    #d. 00011000 00111000 00001101 00001011
    
#作業 5. 課本 Ch3. P3.28
    #a. 234
    #b. 560
    #c. 874
    #d. 888
    
#作業 6. 課本 Ch3. P3.30
    #a. 234
    #b. 560
    #c. 875
    #d. 889



