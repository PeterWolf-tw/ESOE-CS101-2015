#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 繳交日期：2015.11.26

# 作業內容：
# 1. 請參閱 Wikipedia 維基百科 IEEE754 條目 (https://zh.wikipedia.org/wiki/IEEE_754)
# 此題不用繳交，期中/期未考試自然見真章。

# 2. 請試玩 http://armorgames.com/play/17826/logical-element

# 3. 請利用以下空白範本設計一支程式。程式可輸入一段字串，並自動計算出字串中包括空白字元出現的機率。
#    並由高排到低。
def charFreqLister(inputSTR):
    
    
    sum=round(len(inputSTR),1)
    inputSTR = list(inputSTR)
    
    freqA = [round(inputSTR.count('A')/sum,4)]
    freqB = [round(inputSTR.count('B')/sum,4)]
    freqC = [round(inputSTR.count('C')/sum,4)]
    freqD = [round(inputSTR.count('D')/sum,4)]
    freqE = [round(inputSTR.count('E')/sum,4)]
    freqF = [round(inputSTR.count('F')/sum,4)]
    freqG = [round(inputSTR.count('G')/sum,4)]
    freqH = [round(inputSTR.count('H')/sum,4)]
    freqI = [round(inputSTR.count('I')/sum,4)]
    freqJ = [round(inputSTR.count('J')/sum,4)]
    freqK = [round(inputSTR.count('K')/sum,4)]
    freqL = [round(inputSTR.count('L')/sum,4)]
    freqM = [round(inputSTR.count('M')/sum,4)]
    freqN = [round(inputSTR.count('N')/sum,4)]
    freqO = [round(inputSTR.count('O')/sum,4)]
    freqP = [round(inputSTR.count('P')/sum,4)]
    freqQ = [round(inputSTR.count('Q')/sum,4)]
    freqR = [round(inputSTR.count('R')/sum,4)]
    freqS = [round(inputSTR.count('S')/sum,4)]
    freqT = [round(inputSTR.count('T')/sum,4)]
    freqU = [round(inputSTR.count('U')/sum,4)]
    freqV = [round(inputSTR.count('V')/sum,4)]
    freqW = [round(inputSTR.count('W')/sum,4)]
    freqX = [round(inputSTR.count('X')/sum,4)]
    freqY = [round(inputSTR.count('Y')/sum,4)]
    freqZ = [round(inputSTR.count('Z')/sum,4)]
    freqa = [round(inputSTR.count('a')/sum,4)]
    freqb = [round(inputSTR.count('b')/sum,4)]
    freqc = [round(inputSTR.count('c')/sum,4)]
    freqd = [round(inputSTR.count('d')/sum,4)]
    freqe = [round(inputSTR.count('e')/sum,4)]
    freqf = [round(inputSTR.count('f')/sum,4)]
    freqg = [round(inputSTR.count('g')/sum,4)]
    freqh = [round(inputSTR.count('h')/sum,4)]
    freqi = [round(inputSTR.count('i')/sum,4)]
    freqj = [round(inputSTR.count('j')/sum,4)]
    freqk = [round(inputSTR.count('k')/sum,4)]
    freql = [round(inputSTR.count('l')/sum,4)]
    freqm = [round(inputSTR.count('m')/sum,4)]
    freqn = [round(inputSTR.count('n')/sum,4)]
    freqo = [round(inputSTR.count('o')/sum,4)]
    freqp = [round(inputSTR.count('p')/sum,4)]
    freqq = [round(inputSTR.count('q')/sum,4)]
    freqr = [round(inputSTR.count('r')/sum,4)]
    freqs = [round(inputSTR.count('s')/sum,4)]
    freqt = [round(inputSTR.count('t')/sum,4)]
    frequ = [round(inputSTR.count('u')/sum,4)]
    freqv = [round(inputSTR.count('v')/sum,4)]
    freqw = [round(inputSTR.count('w')/sum,4)]
    freqx = [round(inputSTR.count('x')/sum,4)]
    freqy = [round(inputSTR.count('y')/sum,4)]
    freqz = [round(inputSTR.count('z')/sum,4)]
    freq  = [round(inputSTR.count(' ')/sum,4)]
    freq1 = [round(inputSTR.count('1')/sum,4)]
    freq2 = [round(inputSTR.count('2')/sum,4)]
    freq3 = [round(inputSTR.count('3')/sum,4)]
    freq4 = [round(inputSTR.count('4')/sum,4)]
    freq5 = [round(inputSTR.count('5')/sum,4)]
    freq6 = [round(inputSTR.count('6')/sum,4)]
    freq7 = [round(inputSTR.count('7')/sum,4)]
    freq8 = [round(inputSTR.count('8')/sum,4)]
    freq9 = [round(inputSTR.count('9')/sum,4)]
    freq0 = [round(inputSTR.count('0')/sum,4)]
    
    resultLIST = [
    (freqA,"A"),
    (freqB,"B"),
    (freqC,"C"),
    (freqD,"D"),
    (freqE,"E"),
    (freqF,"F"),
    (freqG,"G"),
    (freqH,"H"),
    (freqI,"I"),
    (freqJ,"J"),
    (freqK,"K"),
    (freqL,"L"),
    (freqM,"M"),
    (freqN,"N"),
    (freqO,"O"),
    (freqP,"P"),
    (freqQ,"Q"),
    (freqR,"R"),
    (freqS,"S"),
    (freqT,"T"),
    (freqU,"U"),
    (freqV,"V"),
    (freqW,"W"),
    (freqX,"X"),
    (freqY,"Y"),
    (freqZ,"Z"),
    (freqa,"a"),
    (freqb,"b"),
    (freqc,"c"),
    (freqd,"d"),
    (freqe,"e"),
    (freqf,"f"),
    (freqg,"g"),
    (freqh,"h"),
    (freqi,"i"),
    (freqj,"j"),
    (freqk,"k"),
    (freql,"l"),
    (freqm,"m"),
    (freqn,"n"),
    (freqo,"o"),
    (freqp,"p"),
    (freqq,"q"),
    (freqr,"r"),
    (freqs,"s"),
    (freqt,"t"),
    (frequ,"u"),
    (freqv,"v"),
    (freqw,"w"),
    (freqx,"x"),
    (freqy,"y"),
    (freqz,"z"),
    (freq1,"1"),
    (freq2,"2"),
    (freq3,"3"),
    (freq4,"4"),
    (freq5,"5"),
    (freq6,"6"),
    (freq7,"7"),
    (freq8,"8"),
    (freq9,"9"),
    (freq0,"0"),
    (freq ," ")]
    
    resultLIST.sort(reverse=True)
    print(resultLIST)
    










# 3.1 加分題 (有做有加分，沒做不扣分)：請用課堂中提到的「霍夫曼編碼]
#     (https://zh.wikipedia.org/wiki/霍夫曼編碼) 為你之前設計的
#     程式加上轉碼壓縮的功能。
# e.g.,
#def huffmanTranslater(inputSTR):
#resultLIST = [(freq, char, code), (freq, char, code), (freq, char, code),...]

#return resultLIST


if __name__ == '__main__': 
    
    while True:
        outputLIST=charFreqLister(raw_input("please enter something:"))
       
        
    print (outputLIST)
  
    