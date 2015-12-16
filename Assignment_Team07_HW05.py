#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#請各組於 12/6(日) 午夜前上傳一個 Python 題目至 Github 課程專案內。
#檔名為 Assignment_TeamXX_HW05.py 其中 XX 為你們的組別編號。
#e.g., 第 3 組同學，請上傳 Assignment_Team03_HW05.py 每組上傳一個檔案即可。

#題目可自由發揮，內容亦不限計概。您可以代入其他必修課程中需要運算的部份做為程式計算的步驟，但務必以清楚文字描述。
#參考題型：http://www.ling.gu.se/~lager/python_exercises.html
#若要從前述網頁中出題，1 ~ 16 題因為太簡單，不可列在其中。

...

題目內容：

	設計一支程式，使其在輸入一串互不相等數字之後，輸出其所有可能之排列個數及排列。

輸入說明：

	1.首先輸入一個正整數 n ( 0 < n < 11 )，代表接下來要輸入的數字個數。
	2.接著輸入 n 個正整數 a1, a2, a3,....an ( ai != aj, where 1 < i, j < 11 and i != j )。
	
輸出說明：

	1.輸出 n!。
	2.輸出此 n 個正整數 a1, a2, a3,....an 所有可能之排列。
	
範例輸入：

	3
	1 2 3
	
範例輸出：
	
	6
	1 2 3
	1 3 2
	2 1 3
	2 3 1
	3 1 2
	3 2 1