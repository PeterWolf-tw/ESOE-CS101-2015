#encoding: utf-8

def b2d(n):
    if int(n) >= 0 :
        reminder = 0
        i = 1
        while (n):
            reminder += int(n[-1]) * i
            n = n[:-1]
            i *= 2
        print (reminder)
    else:
        n = n[1:]
        reminder = 0
        i = 1
        while (n):
            reminder += int(n[-1]) * i
            n = n[:-1]
            i *= 2
        print (-reminder)          

if __name__ == '__main__':
    binNumber = "01100101"
    b2d(binNumber)
#作業 2. 課本 Ch2. P2.19 a=10,b=17,c=6,d=8
#作業 3. 課本 Ch2. P2.20 a=14,b=8,c=13,d=4
#作業 4. 課本 Ch2. P2.22 a=00010001 11101010 00100010 00001110,
#b=01101110 00001110 00111000 01001110,
#c=00001110 00111000 11101010 00111000,
#d=00011000 00111000 00001101 00001011
#作業 5. 課本 Ch3. P3.28 a=234,b=560 c=874,d=888
#作業 6. 課本 Ch3. P3.30 a=234,b=560,c=875,d=889