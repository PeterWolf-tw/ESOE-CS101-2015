#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def huffmanTranslater(inputSTR):

    x = inputSTR
    letterLIST = []
    freqcharLIST = []
    codeLIST = []
    resultLIST = []
    NumLIST = []
    
    l = 0
    while len(x) > 0:
        letterLIST.append(x[0])
        k = x.replace(x[0],"")
        #此迴圈會將inputSTR中的與首位字元相同的字元消除
        freq = (len(x)-len(k))*1.0/len(inputSTR)
        #計算長度差，推得該字元出現頻率       
        freqcharLIST.append([freq,letterLIST[l]])  
        x = k
        l += 1
        #做重複動作直到inputSTR不包含任何字元    
    freqcharLIST = sorted(freqcharLIST, reverse=True)
    #製作出letterLIST(含所有出現字元)及freqcharLIST(字母及頻率按頻率大小排)
     
#########以上為第三題，以下為我認知錯誤的Huffman Code > < 不過竟然花了蠻多時間打了就把它放上來吧！######### 
    w = len(letterLIST) - 1
    while w >= 0:
        NumLIST.append(w)
        w -= 1
        NumLIST = sorted(NumLIST)
        #本迴圈製作出NumLIST(從零開始的整數，整數數量與出現字元數相同)
        
    for i in NumLIST:
        codeLIST.append(str(10**i)[::-1])
        #將Code定為10的(頻率大小排名-1)次方的顛倒數列
    codeLIST[len(letterLIST)-1] = (codeLIST[len(letterLIST)-2].replace("1","0"))
    #頻率最小的Code是將頻率次小的Code全部轉換為0
###############################################################################################
        
    for i in NumLIST:
        resultLIST.append(((freqcharLIST[i])[0],(freqcharLIST[i])[1],codeLIST[i]))
        #本迴圈將Freq, Char, Code依序填入resultLIST
    return (resultLIST)

if __name__ == "__main__":
    testSTR01 = "The quick brown fox jumps over the lazy dog"
    result = huffmanTranslater(testSTR01)
    print(result)
    testSTR02 = "Jim quickly realized that the beautiful gowns are expensive"
    result = huffmanTranslater(testSTR02)
    print(result)
    testSTR03 = "a for apple, b for ball!!"
    result = huffmanTranslater(testSTR03)
    print(result)
