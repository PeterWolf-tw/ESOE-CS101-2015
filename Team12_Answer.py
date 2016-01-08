#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#請參考以下空白程式，設計一支程式能讓使用者自行定義輸入的字串為m進位法，並且換算成n進位法(其中，m, n為介於2至61的正整數)
#在此，我們定義大寫英文字母A為10、Z為35;小寫英文字母a為36、z為61，其他字母以此類推
#可不考慮負數及浮點數的計算
#補充說明：需要偵測出輸入字串無法用輸入進位法表示（有在FB上公告）

def m2n(x):
    '''
    本函式將 m 進位制表示數轉為 n 進位制
    '''    
#####################################################################
    char_numberLIST = []
    for i in range(48,123):
        if 47 < i and i < 58:
            char_numberLIST.append(chr(i))
            char_numberLIST.append(i-48)
        elif 64 < i and i < 91:
            char_numberLIST.append(chr(i))
            char_numberLIST.append(i-55)
        elif 96 < i and i < 123: 
            char_numberLIST.append(chr(i))
            char_numberLIST.append(i-61)
 
##############先製作出字串中的字母或數字，對數值的對換表##############
    
    m = int(input("請輸入此字串所使用的進位法："))
    if m > 61 or m < 2:
        return "進位法只能介於2至61之間！"
    x = x[::-1]
    Decimal = 0    
    
    i = 0
    while i < len(x):
        w = char_numberLIST[char_numberLIST.index(x[i])+1]
        if w > m :
            return "此進位法無法表示出這串字串！"
        else:
            Decimal += w*(m**i)
        i += 1
#########先偵測輸入有無錯誤，若無錯誤則將字串先改為十進位表示法#########

    n = int(input("請輸入想要以何種進位法表達：")) 
    if n > 61 or n < 2:
        return "進位法只能介於2至61之間！"
    tmpLIST = []
    while Decimal > 0:
        remainder = int(Decimal % n)
        tmpLIST.append(char_numberLIST[char_numberLIST.index(remainder)-1])
        Decimal = (Decimal - remainder) / n

    ans = ""
    for j in tmpLIST[::-1]:
        ans = ans + str(j)
    return ans
#####################將十進位表示法改為指定的表示法#####################
  
if __name__ == "__main__":
   
    testSTR = input("請輸入字串：")
    result = m2n(testSTR)
    print(result)

# ===== Team12 =====
# Team01: Fail ("放棄作答")
# Team02: Fail ("放棄作答")
# Team03: Fail ("無法執行")
# Team04: Fail ("放棄作答")
# Team05: -    ("若輸入字串有z，則字串無法成功轉換")
# Team06: Fail ("放棄作答")
# Team07: Fail ("以C++作答")
# Team08: Fail ("無法偵測出輸入字串不得用輸入進位法表達。沒有主程式，無法輸入字串")
# Team09: Fail ("若輸入字串有z，則字串無法成功轉換。沒有主程式，無法輸入字串。無法偵測輸入的進位法介於2至61")
# Team10: Fail ("放棄作答")
# Team11: Fail ("若輸入字串有z，則字串無法成功轉換。沒有主程式，無法輸入字串")
# Team13: Fail ("無法偵測出輸入字串不得用輸入進位法表達")
# Team14: Fail ("放棄作答")
    
