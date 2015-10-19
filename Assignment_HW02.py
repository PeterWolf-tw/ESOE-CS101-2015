#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import math

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




#作業 2. 課本 Ch2. P2.19
Ch2P2_19a = 10
Ch2P2_19b = 17
Ch2P2_19c = 6
Ch2P2_19d = 8

def minBit(lessThanNumber):
    '''
    若將求解方式寫成函式
    '''
    i = 0
    while 2**i < lessThanNumber:
        i = i+1
    return i

#作業 3. 課本 Ch2. P2.20
Ch2P2_20a = 14
Ch2P2_20b = 8
Ch2P2_20c = 13
Ch2P2_20d = 4

def kDigit(num, base):
    '''
    若將求解方式寫成函式
    '''
    k = int(math.log(num, base))
    return k

#作業 4. 課本 Ch2. P2.22
Ch2P2_22a = "00010001 11101010 00100010 00001110"
Ch2P2_22b = "00001110 00111000 11101010 00111000"
Ch2P2_22c = "01101110 00001110 00111000 01001110"
Ch2P2_22d = "00011000 00111000 00001101 00001011"

def int2binByBase(N, bitLength):
    '''
    本函式修改自 int2bin()，將 int 整數轉為 bin 二進位制表示，並依 baseLength 調整向前補 0
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

    if len(ans) == 8:
        pass
    elif len(ans) > 8:
        ans = ans[1:]
    else:
        while len(ans) < 8:
            ans = "0" + ans
    return ans

#作業 5. 課本 Ch3. P3.28
Ch3P3_28a = 234
Ch3P3_28b = 560
Ch3P3_28c = 874
Ch3P3_28d = 888

def ninesComplement(inputSTR):
    ans = ""
    if inputSTR[0] == "-":
        for i in inputSTR[1:]:
            ans = ans + str(9 - int(i))
    else:
        if inputSTR[0] == "+":
            ans = inputSTR[1:]
        else:
            ans = inputSTR
    return ans

#作業 6. 課本 Ch3. P3.30
Ch3P3_30a = 234
Ch3P3_30b = 560
Ch3P3_30c = 875
Ch3P3_30d = 889

def tensComplement(inputSTR):
    ans = ""
    if inputSTR[0] == "-":
        for i in inputSTR[1:]:
            ans = ans + str(9 - int(i))
        ans = str(int(ans)+1) # ten's complement 和 nine's complement 唯一的不同之處。
    else:
        if inputSTR[0] == "+":
            ans = inputSTR[1:]
        else:
            ans = inputSTR
    return ans

if __name__ == '__main__':
    intNumber = 100
    int2bin(intNumber)

    binNumber = "01100101"
    #bin2int(number)

    # ###########################
    print("Ch2P2_19:")
    print("a.", minBit(1000))
    print("b.", minBit(100000))
    print("c.", minBit(64))
    print("d.", minBit(256))
    print("======================")
    # ###########################
    print("Ch2P2_20:")
    print("a.", kDigit(2**14, 2))
    print("b.", kDigit(10**8, 10))
    print("c.", kDigit(8**13, 8))
    print("d.", kDigit(16**4, 16))
    print("======================")
    # ###########################
    print("Ch2P2_22:")
    print("a.", int2binByBase(17, 8), int2binByBase(234, 8), int2binByBase(34, 8), int2binByBase(14, 8))
    print("b.", int2binByBase(14, 8), int2binByBase(56, 8), int2binByBase(234, 8), int2binByBase(56, 8))
    print("c.", int2binByBase(110, 8), int2binByBase(14, 8), int2binByBase(56, 8), int2binByBase(78, 8))
    print("d.", int2binByBase(24, 8), int2binByBase(56, 8), int2binByBase(13, 8), int2binByBase(11, 8))
    print("======================")
    # ###########################
    print("Ch3P3_28:")
    print("a.", ninesComplement("+234"))
    print("b.", ninesComplement("+560"))
    print("c.", ninesComplement("-125"))
    print("d.", ninesComplement("-111"))
    print("======================")
    # ###########################
    print("Ch3P3_30:")
    print("a.", tensComplement("+234"))
    print("b.", tensComplement("+560"))
    print("c.", tensComplement("-125"))
    print("d.", tensComplement("-111"))
    print("======================")