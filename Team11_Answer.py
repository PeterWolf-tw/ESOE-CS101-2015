#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import random

def team11():
    while True:
        people=["2","3","4","5"]
        level=[]
        A=["+1","+2","+3","return","pass"]
        B=["+1","+2","+3"]
        counter = 0
        clockwide =True
        value = 0
        while True:
            n=input("共有多少人參與遊戲??")
            if n not in people:
                print("87??")
                continue
            else:
                break
        n=int(n)
        for i in range(n):
            level.append(2)
        person = random.randint(1,n)
        number = random.randint(1, 36)
        level[person-1] -= 1
        print("To player",person)
        ABC = input("you can type anything to get the number.")
        print("the number is ",number)
        DEF = input("and you can type anything to hide the number.")
        print("878787878787878787878787878787878787878787878787878787878787878787")
        print("878787878787878787878787878787878787878787878787878787878787878787")
        print("878787878787878787878787878787878787878787878787878787878787878787")
        print("878787878787878787878787878787878787878787878787878787878787878787")
        print("878787878787878787878787878787878787878787878787878787878787878787")
        print("878787878787878787878787878787878787878787878787878787878787878787")
        print("878787878787878787878787878787878787878787878787878787878787878787")
        print("878787878787878787878787878787878787878787878787878787878787878787")
        print("878787878787878787878787878787878787878787878787878787878787878787")        
        while True:
            if level[person-1] == 2:
                print("player",person,",now count to ",value)
                while True:
                    ins = input("you can input +1,+2,+3,return or pass.")
                    if ins not in A:
                        print("87")
                        continue
                    elif ins == "+1"or ins =="+2" or ins =="+3":
                        ins = int(ins[1])
                        value += ins
                        break
                    elif ins == "return":
                        clockwide = not clockwide
                        level[person-1] -= 1
                        break
                    else:
                        level[person-1] -= 1
                        break
        
            else:
                print("player",person,",now count to ",value)
                while True:
                    ins = input("you can input +1,+2,+3.")
                    if ins not in B:
                        print("87")
                        continue
                    else:
                        ins = int(ins[1])
                        value += ins
                        break
            if value >= number:
                print("player",person," NI太嫩ㄌ 答案是", number)
                break
            
            if clockwide == True:
                person+=1
            else:
                person-=1
            if person > n:
                person-=n
                
            elif person == 0:
                person += n
            continue
        WTF = input("type anything to start another game!")
        continue

#判定結果
# ===== Team11 =====
# Team01: Fail (未作答)
# Team02: Fail (未作答)
# Team03: Fail (未作答)
# Team04: Fail (未作答)
# Team05: Pass
# Team06: Fail (未限制指令範圍,未做出迴轉及跳過指令)
# Team07: Fail (未作答)
# Team08: Fail (未限制指令範圍,未做出迴轉及跳過指令)
# Team09: Fail (未做出迴轉指令,未能控制跳過指令使用次數)
# Team10: Fail (未作答)
# Team12: Pass 
# Team13: Fail (迴轉指令沒有做好做滿,過邊界時會有問題)
# Team14: Fail (未作答)
if __name__ == "__main__":
    team11()