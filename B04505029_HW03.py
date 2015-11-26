#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 3. 請利用以下空白範本設計一支程式。程式可輸入一段字串，並自動計算出字串中包括空白字元出現的機率。
#    並由高排到低。
#def charFreqLister(inputSTR):
#resultLIST = [(freq, char), (freq, char), (freq, char),...]

def charFreqLister(inputSTR):
    testSTR = inputSTR                #宣告變數testSTR為input
    testlist = []                     #宣告testlist為一空list
    testlist = list(testSTR)          #將testSTR字串排入list
    sortlist = []                     #宣告sortlist為一空list
    sortlist = sorted(testlist)       #將tsetlist內的字元排序並輸入sortlist,以便等等設計迴圈消除testlist內的重複字元
    length = len(sortlist)            #宣告變數length為sortlist的長度
    remainlist = []                   #宣告remainlist為一空list,以放入不重複字元
    remainlist.append(sortlist[0])    #將sortlist的第一字元排入remainlist
    wkchar = str(sortlist[0])         #宣告變數wkchar=sortlist的第一字元,即將字元放入暫存變數workrecord
    for i in range(0,length):         #從以下迴圈開始刪除重複字元
        if wkchar != str(sortlist[i]):
            wkchar = str(sortlist[i]) #如果wkchar與即將輸入字元不相等,則將其輸入,否則pass
            remainlist.append(sortlist[i]) #將不相等字元加入remainlist
    lengthr = len(remainlist)              #宣告變數lengthr為remainlist長度
    newlist = []                           #宣告newlist為空list,用來輸入字元與它的出現次數
    resultlist = []                        #宣告resultlist為空list,用來輸入最後結果
    for i in range(0,lengthr):             #以下迴圈開始計算input中各字元出現次數
        freqSTR = testlist.count(remainlist[i])   #宣告freqSTR為remainlist的第i+1個字元在testlist中出現的次數
        newlist.append((freqSTR,remainlist[i]))
    resultlist = sorted(newlist, reverse=True, key = lambda x :x[0])  #將最終結果依freqSTR排序並由高到低
    

    return resultlist


# 3.1 加分題 (有做有加分，沒做不扣分)：請用課堂中提到的「霍夫曼編碼]
#     (https://zh.wikipedia.org/wiki/霍夫曼編碼) 為你之前設計的
#     程式加上轉碼壓縮的功能。
# e.g.,
#def huffmanTranslater(inputSTR):
#resultLIST = [(freq, char, code), (freq, char, code), (freq, char, code),...]

#return resultLIST

class Node:                                                                      #Tree-Node Type 節點定義
    def  __init__ (self, freq, char, left = None, right = None, father = None):  #定義起始點與其中用到的變數
        self.left  = left 
        self.right = right 
        self.father= father 
        self.char  = char 
        self.freq  = freq 

def createHuffmanTree(freqschars):                        #定義Huffman樹(使用上一題的結果做為input)
    node_list = [Node (* pair ) for  pair in  freqschars] #宣告node_list內含節點的Node資料
     
    while len(node_list) > 1:                             #利用此迴圈開始建構Huffman樹,即當node_list中有多於一項時:往下執行迴圈
        node_list.sort(key = lambda item : item.freq)     #先將node_list內的項目依freq排序(由低至高)
        left  = node_list.pop(0)                          #pop(0):刪除字串中第一個項目,並把這個值給left 
        right = node_list.pop(0)                          #pop(0):刪除剩下字串中第一個項目,並把這個值給right
        father= Node(left.freq + right.freq, left.char + right.char, left, right)  #將father訂為兩freq最小的加總節點 
        left.father = father 
        right.father= father 
        node_list.append(father)                          #將父節點加入node_list

    return  node_list[0]                                  #回傳最後結果(只剩一項)

def huffmanEncode(char, tree):                            #宣告huffmanEncode函數(做為Huffman編碼用)  
    code = ''                                             #宣告變數code為空字串
    while tree.left :                                     
        if  char in tree.left.char :                      #當char是在左節點時
            code += '0'                                   #將0代入code
            tree =  tree.left                             
        else : 
            code += '1'                                   #反之,右節點代1
            tree = tree.right 
    return  code 

def huffmanTranslater(freqschars):                        #定義新函數:Huffman字串轉碼壓縮  
    codes =[]                                             #宣告codes為空list
    for item in freqschars:
        codes.append((item[0], item[1], huffmanEncode(item[1],Hufftree )))  #依題意要求將所需輸入codes 
    
    
    return  codes 


if __name__ == "__main__":
    testSTR01 = "The quick brown fox jumps over the lazy dog"
    result = charFreqLister(testSTR01)
    print(result)
    Hufftree = createHuffmanTree(result)
    resultLIST = huffmanTranslater(result)
    print(resultLIST)
    testSTR02 = "Jim quickly realized that the beautiful gowns are expensive"
    result = charFreqLister(testSTR02)
    print(result)
    Hufftree = createHuffmanTree(result)
    resultLIST = huffmanTranslater(result)   
    print(resultLIST)