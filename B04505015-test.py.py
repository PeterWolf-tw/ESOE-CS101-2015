# -*- coding:utf-8 -*- 
  
#number = 100 #設定 number 這個變數的值為 2 
#print(bin(number)) #將 2 餵入 bin(n) 函式中，並把 bin(n) 回傳的結果，接著餵給 print() 輸出在螢幕畫面上。 
  
# 你可以試著把 number 的值改為其它的數字，觀察看看。 
  
# bin(n) 的原理大致如下： 
  
def int2bin(N): 
    ''' 
    本函式將 int 整數轉為 bin 二進位制表示 
    ''' 
    inNum= N
    tmpLIST = [] 
    while N > 0: 
        remainder = int(N % 2) 
        tmpLIST.append(remainder) 
        N = (N - remainder) / 2 
    tmpLIST.append(0) 
  
    ans = "" 
    for j in tmpLIST[::-1]: #將 tmpLIST 中的數字從尾至頭傳入 j 
        ans = ans + str(j) 
    print("{0} 的二進位表示為 {1}.".format(inNum, ans)) 

    return None 
  
  
#========== 作業 1.========== 
# 請參考上例，自己寫一個將二進位表示數轉為十進位制的函式： 
def bin2int(Str):
    '''
    本函式將 bin 二進位制表示數轉為 int 整數 
    '''
    ans= 0 
    baseNum= 1
  
    for j in Str[::-1]: #將 Str 中的字元從尾至頭傳入 j 
        ans += int(j)* baseNum
        baseNum *= 2
    print("{0} 的十進位表示為 {1}.".format(Str, ans)) 
    
  
    return None 
#========== 作業 1.========== 
  
  
if __name__ == '__main__': 
    intNumber = 100 
    int2bin(intNumber) 
  
    binNumber = "01100101" 
    bin2int(binNumber) 
