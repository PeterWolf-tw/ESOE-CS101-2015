#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#Python 程式的前兩行是固定的，請牢記。


#第一題
#輸入一二進位表示法的整數數值m
#函數f(a)將會把m表示為十進位表示法n


p=0
print("若輸入負的非二位數表示法則可停止運算")
while(p==0):

    def f(a):

        if (a>=0): a*=1
        else: a*=-1    #進入迴圈前先把數值變為正，最後顯示在補回正負
        i=0    #(i+1) 為目前進行的迴圈次數
        n=0


        while (a>=1):
            x=a%10
            if(x<=1):
                k=x*(2**i)
                i+=1
                a=a//10
                n+=k
            else:
                print("Failed Input")
                return("")

        return n

    m = int(input("\n以二進位表示法為: "))

    if(m>=0):
        #print ("以十進位表示法為:"),f(m),("\n")
        print ("以十進位表示法為:",f(m),"\n")

    else:
        #print ("以十進位表示法為:"),-f(m),("\n")
        print ("以十進位表示法為:",-f(m),"\n")
    #print() 的內容全部放在它的括號裡。在括號裡用半形逗點隔開即可。

    p=input("如需再做計算請輸入0 \n")
    #這個設計很棒，不過好像沒有作用。


#第二題
#Ch.2 P2.19 a=10
#Ch.2 P2.19 b=17
#Ch.2 P2.19 c=6
#Ch.2 P2.19 d=8

#第三題
#Ch.2 P2.20 a=14
#Ch.2 P2.20 b=8
#Ch.2 P2.20 c=13
#Ch.2 P2.20 d=4

#第四題
#Ch.2 P2.22 a=00010001 11101010 00100010 00001110
#Ch.2 P2.22 b=00001110 00111000 11101010 00111000
#Ch.2 P2.22 c=01101110 00001110 00111000 01001110
#Ch.2 P2.22 d=00011000 00111000 00001101 00001011

#第五題
#Ch.3 P3.28 a=234
#Ch.3 P3.28 b=560
#Ch.3 P3.28 c=874
#Ch.3 P3.28 d=888

#第六題
#Ch.3 P3.30 a=234
#Ch.3 P3.30 b=560
#Ch.3 P3.30 c=875
#Ch.3 P3.30 d=889
