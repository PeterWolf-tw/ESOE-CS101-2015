def bin2int(N):
    n = str(N)
    an = 0
    p = 0
    while p < len(n):
        if n[p] == '1':
            an += 2 ** (len(n) - 1 - p)
        p += 1
    return an
#P2-19
#a. 10bits
#b. 17bits
#c. 6bits
#d. 8bits
#P2-20
#a. 14digits
#b. 8digits
#c. 13digits
#d. 4digits
#P2-22
#a. 00010001 11101010 00100010 00001110
#b. 00001110 00111000 11101010 00111000
#c. 01101110 00001110 00111000 01001110
#d. 00011000 00111000 00001101 00001011
#P3-28
#a. 280
#b. 682
#c. 741
#d. 756
#P3-29
#a. -500 ~ 499
#b. If the first digit is greater than 4, it's negative, otherwise, positive.
#c. No
#d. 000
