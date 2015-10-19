# !/usr/bin/env python3
#  -*- coding:utf-8 -*-


#第一題
j = 1
def bin2int(x):
    '''
    本函式將 bin 二進位制表示數轉為 int 整數
    '''
    value = 0
    value1 = 0
    r = 10
    k = 0
    while (x>=1):
        i = x%r
        if (i<=1):
            value1 += i*(2**k)
            k += 1
            x = x//r
        else:
            print ("輸入的數不為2進制數")
            return "none"
        value = value1
    while (x<=-1):
        x = -x
        i = x%r
        if (i<=1):
            value1 += i*(2**k)
            k += 1
            x = -(x//r)
        else:
            print ("輸入的數不為2進制數")
            return "none"
        value = -value1
    return value

if __name__ == "__main__":
#請加上程式進入點。
    while (j==1):
        a = input("請輸入一2進制數:")
        a = int (a)
        print ("此數以十進制表示為:",bin2int(a),"\n")
        #若能配合某個退出設定會更好。e.g., 「按下 Q 鍵中止程式」。


#第二題 P2-19
#a. 10
#b. 17
#c. 6
#d. 8

#第三題 P2-20
#a. 14
#b. 8
#c. 13
#d. 4

#第四題 P2-22
#a.00010001 11101010 00100010 00001110
#b.00001110 00111000 11101010 00111000
#c.01101110 00001110 00111000 01001110
#d.00011000 00111000 00001101 00001011

#第五題 P3-28
#a.234
#b.560
#c.874
#d.888

#第六題 P3-30
#a.234
#b.560
#c.875
#d.889