#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#Python 程式的前兩行是固定的，請牢記。

'''
1.Binary-to-Decimal Transfer Function
'''
#Check if the input is valid
#Python 的縮排是空四格。下次請採用空四格的方式做縮排。
#Python 也不需在行尾加分號做為終結。

def check_input(s):
	if(s == "."):
		return False;
	for i in range (0,len(s)):
		if(s[i] == '0' or s[i] == '1' or s[i] == '.'):
			continue;
		else:
			return False;
	return True;
#Check if there is decimal point
def check_dcp(s):
	for i in range (0,len(s)):
		if(s[i] == '.'):
			return i;
	return -1;
#Transfer function
def btd(s):
	d = 0.0;
	if(check_dcp(s) == -1):
		for i in range (0,len(s)):
			if(s[i] == '1'):
				d += (2**(len(s)-1-i));
	else:
		for i in range (0,check_dcp(s)):
			if(s[i] == '1'):
				d += (2**(check_dcp(s)-i-1));
		for i in range (check_dcp(s)+1,len(s)):
			if(s[i] == '1'):
				d += (2**(check_dcp(s)-i));
	return d;
#Main function
print("Welcome to the Binary-to-Decimal transfer system. Enter -1 if you want to end.");
while True :
	#binary = raw_input("Please enter a binary number: ");
	binary = input("Please enter a binary number: ");
	#raw_input() 是 Python2 的寫法。在 Python3 裡已經全部改為 input() 了。
	if(binary == "-1"):
		print("Thanks for using. Good bye!");
		break;
	if(check_input(binary) == True):
		print("The decimal value of the number is  %.4f" %(btd(binary)));
	else:
		print("Invalid input.");

'''
2.P2-19
	a.10
	b.17
	c.6
	d.8
3.P2-20
	a.14
	b.8
	c.13
	d.4
4.P2-22
	a.00010001 11101010 00100010 00001110
	b.00001110 00111000 11101010 00111000
	c.01101110 00001110 00111000 01001110
	d.00011000 00111000 00001101 00001011
5.P3-28
	a.234
	b.560
	c.874
	d.888
6.P3-30
	a.234
	b.560
	c.875
	d.889
'''