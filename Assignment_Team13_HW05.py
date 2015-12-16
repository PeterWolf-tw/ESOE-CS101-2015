#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#請各組於 12/6(日) 午夜前上傳一個 Python 題目至 Github 課程專案內。
#檔名為 Assignment_TeamXX_HW05.py 其中 XX 為你們的組別編號。
#e.g., 第 3 組同學，請上傳 Assignment_Team03_HW05.py 每組上傳一個檔案即可。

#題目可自由發揮，內容亦不限計概。您可以代入其他必修課程中需要運算的部份做為程式計算的步驟，但務必以清楚文字描述。
#參考題型：http://www.ling.gu.se/~lager/python_exercises.html
#若要從前述網頁中出題，1 ~ 16 題因為太簡單，不可列在其中。


'''
在權力遊戲中，我們可以看到Stark和Lannister兩大家族激烈的鬥爭。以下為兩大家族一小部分的成員以及彼此間的主從關係。請設計一支程式
當我們輸入任兩人時能夠自動解得兩人間的關係
(長官、屬下、平輩(即兩人直屬長官不同但屬於同一家族或直屬長官相同且彼此間非主從關係)、敵人(即兩人分屬不同家族)、資料有誤無法比對)
e.g.
Jon Snow 與Bran Stark 為平輩(因為兩人接隸屬於Eddard Stark之下，
但是Jon Snow 的直屬長官為 Robert Stark 所以Jon Snow 與Bran Stark 視為平輩)

Hodor 與 Robert Stark 為平輩
Eddard Stark 與 Jamie Lannister 為敵人
Tywin Lannister 為 Jamie Lannister 的長官

ID代碼  名稱          長官ID代碼
100,     Jon Snow,       200
200,     Robert Stark,    300
300,     Eddard Stark,    300
400,     Bran Stark,      300
500,     Tywin Lannister,  500
600,     Jamie Lannister,  500
800,     Ser Rodrik,      200
900,     Hodor,          400
700,     Rhaegar Targaryen, 000
'''
