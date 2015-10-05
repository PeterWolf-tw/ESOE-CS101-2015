#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 以 "#" 字符號開頭的內容將被 Python 視為「註解」。不會執行。

# #########################################說明########################################
# 對 Python 而言， if __name__ == "__main__" 即為程式的進入點。換言之，整支程式從這一行開始執行。

#def sayHi():
    #'''
    #這裡定義了一個函式，名叫 sayHi
    #'''
    # #這支函式唯一的功能就是印出下面這一句話…
    #print("Hi！這是一支只會說 Hi 的函式。")



#if __name__ == '__main__': #這裡是程式進入點。整支程式從這裡開始執行…
    # #以下執行 sayHi() 函式
    #sayHi()

# #####################################################################################

# 作業內容：
# Python 本身已有一將整數轉換為二進位制的函式 bin(n) 可將整數 n 換為二進位制的表示式：
# e.g.,

number = 100  #設定 number 這個變數的值為 2
print(bin(number)) #將 2 餵入 bin(n) 函式中，並把 bin(n) 回傳的結果，接著餵給 print() 輸出在螢幕畫面上。

# 你可以試著把 number 的值改為其它的數字，觀察看看。

# bin(n) 的原理大致如下：

def int2bin(N):
    '''
    本函式將 int 整數轉為 bin 二進位制表示
    '''
    tmpLIST = []
    while N > 0:
        remainder = int(N % 2)
        tmpLIST.append(remainder)
        N = (N - remainder) / 2
    tmpLIST.append(0)

    ans = ""
    for j in tmpLIST[::-1]: #將 tmpLIST 中的數字從尾至頭傳入 j
        ans = ans + str(j)
    print("{0} 的二進位表示為 {1}.".format(N, ans))
    return None


#作業 1.
# 請參考上例，自己寫一個將二進位表示數轉為十進位制的函式：
def bin2int(N):
    '''
    本函式將 bin 二進位制表示數轉為 int 整數
    '''

    return None


if __name__ == '__main__':
    intNumber = 100
    int2bin(intNumber)

    binNumber = "01100101"
    #bin2int(number)

#作業 2. 課本 Ch2. P2.19
#作業 3. 課本 Ch2. P2.20
#作業 4. 課本 Ch2. P2.22
#作業 5. 課本 Ch3. P3.28
#作業 6. 課本 Ch3. P3.30


