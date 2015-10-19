# !/usr/bin/env python3
#  -*- coding:utf-8 -*-

#下次想寫第二解、第三解…乃至第 N 解時，請寫在同一個檔案裡即可。

def bin2int(x):
    decimal = 0
    value = 1
    if x >= 0:
        x = x
        while x > 0:
            remainder = x % 10
            if remainder == 1:
                decimal = decimal + value
            elif remainder == 0:
                decimal = decimal
            else:
                print("QQ 你輸入的不是二進位數喲")
                import sys
                sys.exit()
            value = value * 2
            x = x // 10
        return decimal
    else:
        x = - x
        while x > 0:
            remainder = x % 10
            if remainder == 1:
                decimal = decimal + value
            elif remainder == 0:
                decimal = decimal
            else:
                print("QQ 你輸入的不是二進位數喲")
                import sys
                sys.exit()
            value = value * 2
            x = x // 10
        return -decimal

if __name__ == '__main__':
    x = int(input("請輸入一個二進位數:"))
    print("此二進位數的值為:",bin2int(x))




