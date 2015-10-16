#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import sys

# 示範字串操作。注意 len() 可計算長度。
#print("中文測試")
#s = "這是一串中文字"
#print(len(s))
#print(s)


# 示範字典的操作
#myDict  = {"張先生":"0953xxxxxx", "陳小姐":"0927xxxxxx", 3:"三"}
#print(myDict["張先生"])
#print(myDict[3])


# 字串/數字示範
#x = "1"
#y = "2"
#print(x+y+": 這是兩個數字字符，不是一組數字值哦！")
#a = 1
#b = 2
#print(x+y, ": 這是兩個數字值的相加和，不是兩個數字字符哦！") #請特別注意在 print() 中，因為 x+y 是數字，而後面的說明是字串，所以不用 + 號相連。


#示範字串 (string) 的每個元素都可以被遞迴呼叫的特性
#myString = "This is a very very very long string for demo."
#for i in myString:
    #print(i)


#示範字串可以直接切成列表 list 的特性
#myStringLIST = myString.split(" ")
#print(myStringLIST)


#示範列表可利用 .append() 來增加列表內元素的特性
#myStringLIST = []
#for wr in myString.split(" "):
    #myStringLIST.append(wr)
    #print(myStringLIST)


#示範列表內容可利用迴圈呼叫，一一處理的特性。
#thisClass = [55, 53, 44, 75, 66]
#for i in thisClass:
    #print(i+20)


#示範列表內容可利用其位置 (從 0 起算) 加以呼叫的特性。
#print(thisClass[0])
#print(thisClass[3])
#print(thisClass[-4])
#print(thisClass[0:4])


# 示範 if...elif...elif...else
#for word in myStringLIST:
    #if "e" in word:
        #print(word)
    #else:
        #print("沒有哦")


def mySuperAdder(x, y):
    return x+y


#這是一個可以加三個東西的function
def mySuperAdder2(x, y, z):
    return x+y+z


def myAdder(x, y):
    '''
    function 的註解可以直接用三個單引號加註！
    '''
    return int(x)+int(y)


if __name__ == "__main__":
    # 方法一
    #利用 input() 取得使用者輸入。
    a = int(input("請輸入第一個數字：")) #因為 input() 從使用者介面收進來的都是字串，所以要再經過 int() 轉成整數。
    b = int(input("請輸入第二個數字："))
    # ####################


    # 方法二
    #利用第五行 import 進來的 sys 模組，即可呼叫 sys.argv 來取得在 cmd.exe/Terminal 裡下的參數。
    #e.g., "python py3Demo.py 7 8" 如此一來 a, b 就會分別被指派為 7 和 8
    #a = int(sys.argv[1])
    #b = int(sys.argv[2])
    # ####################


    # 方法三
    #直接寫死指定 a, b, 的值。
    #a = 4
    #b = 5
    # ####################
    ans = mySuperAdder(a, b)
    print("{0} + {1} 是 {2}".format(a, b, ans))