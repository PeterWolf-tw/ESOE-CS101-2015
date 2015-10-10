#!/usr/bin/env python 3
#-*- coding:utf-8 -*-

def bin2int(N):
    '''
    本函式將 bin 整數轉為 int 十進位制表示
    '''

    strN = str(binNumber)                    #宣告變數strN,將input N轉為字串
    strN = [int(j) for j in strN]            #將strN的字元排為陣列
    lengthN=len (strN)                       #宣告變數length,取出strN之位數
    expo = lengthN                           #宣告變數expo=lengthN位數
    k = (-1) * lengthN                       #宣告變數k=-lengthN
    i = 1
    
    x = 0

    if strN[0] == 0:
        while i <= lengthN:
            expo -= 1                        #宣告變數expo=lengthN - 1
            a = strN[k]                      #宣告變數a=strN的右邊數來第k位數值
            x += int(a)*pow(2,expo)
            k += 1

            i += 1
        print("{0} 的十進位表示為 {1}.".format(binNumber, x))
    
    
       
    return None

if __name__ == '__main__':
    binNumber = "01100100"
    
    bin2int(binNumber)
    
    
    







#p2-19a=10
#p2-19b=17
#p2-19c=6
#p2-19d=8
#p2-20a=14
#p2-20b=8
#p2-20c=13
#p2-20d=4
#p2-22a=00010001 11101010 00100010 00001110
#p2-22b=00001110 00111000 11101010 00111000
#p2-22c=01101110 00001110 00111000 01001110
#p2-22d=00011000 00111000 00001101 00001011
#p3-28a=234
#p3-28b=560
#p3-28c=874
#p3-28d=888
#p3-30a=234
#p3-30b=560
#p3-30c=875
#p3-30d=889