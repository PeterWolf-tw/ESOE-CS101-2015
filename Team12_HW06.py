#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#程式以上面兩行開始，從第一次作業講到最後一次，都沒改進。
#這部份曾在 HW02 ~ 03 之間改進，最後一次又出現這個問題。

def BubbleSorting(intlist):
    for Number in range(len(intlist)-1,0,-1):
        for i in range(Number):
            if intlist[i] < intlist[i+1]:
                n = intlist[i]
                intlist[i] = intlist[i+1]
                intlist[i+1] = n


#以前都會記得寫程式進入點 if __name__ == '__main__': 但這次卻沒寫，何以故？

intlist = [5, 16, 20, 3, 8, 12, 9, 17, 20, 7]
BubbleSorting(intlist)
print(intlist)
