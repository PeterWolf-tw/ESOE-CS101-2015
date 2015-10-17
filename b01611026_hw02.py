#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def bin2int(N):
	#本函式將bin轉換成int十進制
    #Python 的縮排以「空四個空格」為主。請避免使用 TAB 做為縮排用。
	tmpList=[N]
	leng=len(N)
	tmpList.reverse(N)
	ans=0
	while leng>0
        #while, for, if...等需要縮排的語法，要在後面加 : 冒號。
		x=tempList.pop()
		ans=ans+x*2**leng
		leng=leng-1

	print binum"的二進位表示為"
	print ans
    return None

if __name__ == '__main__':
	binum=1011
	N=str(binum)
	bin2int(binum)



# p2-19a=   10
# p2-19b=   17
# p2-19c=   6
# p2-19d=   8

# p2-20a=   14
# p2-20b=   8
# p2-20c=   13
# p2-20d=   4

# p2-22a=  00010001  11101010  00100010  00001110
# p2-22b=  00001110  00111000  11101010  00111000
# p2-22c=  01101110  00001110  00111000  01001110
# p2-22d=  00011000  00111000  00001101  00001011

# p3-28a=   234
# p3-28b=   560
# p3-28c=   874
# p3-28d=   888

# p3-30a=   234
# p3-30b=   560
# p3-30c=   875
# p3-30d=   889