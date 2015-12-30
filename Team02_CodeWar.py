#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Assignment_Team01


print ('PLEASE ENTER AN INTEGER')
def Com_Div(n):
    for i in range(1,n):
        if (n%i==0): 
            print(i)
            i+=1
    return n
if __name__ == '__main__':
        n=int(input())
        print(Com_Div(n))


#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Assignment_Team03


alph=input()
l=[]
name_list= ['Bard','Charles','Dennis','Harvey','Mark','Mike','Oliver','Paul','Ryan']
class Friends:

    def __init__(self, data = None):
        if data == None:
            name_list= ['Bard','Charles','Dennis','Harvey','Mark','Mike','Oliver','Paul','Ryan']
              
    def names(self,data = None):
        import random
        print(random.sample(name_list, 3))
            
    def connected(self, alph):
        i=0
        for i in name_list,i<=8 :
            if (alph in name_list[i]):
                l.append[name_list[i]]
            else:
                l.append[None]
            i=i+1    
        return l    
    
      if l=None: 
        print ('no according ones') 
        else :
    print(l) 
        
if __name__ == '__main__':
    old_friends= Friends()
    old_friends.names()
    old_friends.connected(alph)
    
    new_friends=Friends()
    new_friends.names()
    new_friends.connected(alph)



    #!/usr/bin/env python
# -*- coding: utf-8 -*-

# Assignment_Team14


number = input('請輸入費氏數列第n項: ')
n=int(number)
i=1
l = []
a, b = 0, 1
while i<=n:
    l.append(b)
    a, b = b, a+b
    i=i+1
print ('前 ' + str(number) + ' 項為 '+ str(l))
print ('第 ' + str(number) + ' 項之值為 '+ str(l[-1]))


#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Assignment_Team06


import math    
list_1= []
list_2 = []
list_3 = []

def Stand_Dev():
    list_1 = input("輸入任一組數字開始計算標準差 數字間以逗號隔開:").split(",")
    list_1[:] = [float(a) for a in list_1]
    
    avg = sum(list_1)/len(list_1)
    
    for i in range (0,len(list_1),1):
        list_2.append(list_1[i] - avg)
        list_2[:] = [float(a) for a in list_2]
        
    for i in range (0,len(list_2),1):
        list_3.append(math.pow(list_2[i],2))
        list_3[:] = [float(a) for a in list_3]
        
        
    ans = math.sqrt(sum(list_3) / len(list_3))
    print (ans)  
    
if __name__== "__main__":

    n =Stand_Dev()
    print(n)    



 #! /usr/bin/env python
#coding:utf-8


# Assignment_Team08


import random

def drawBoard(board):

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():

    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('選擇 X 或 O?')
        letter = input().upper()


    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():

    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():

    print('再來阿? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):

    return ((bo[7] == le and bo[8] == le and bo[9] == le) or 
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or 
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or 
    (bo[9] == le and bo[5] == le and bo[1] == le))

def getBoardCopy(board):

    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):

    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('輸入下一步 (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):

    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):

    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i


    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move


    if isSpaceFree(board, 5):
        return 5


    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):

    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('九宮格遊戲')

while True:

    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print( turn + ' 先')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player's turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('你贏了')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('平手')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('嫩')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('平手')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
        



 #! /usr/bin/env python
#coding:utf-8


# Assignment_Team09


print ('猜數字遊戲，請輸入4位數字')
print ('A後的數字代表正確的量，B後面則代表錯誤的量')
print ('number=')

import random
l=range(0,9)
n=list(input())
c=0
ans=random.sample(l, 4)

if __name__ == '__main__':
    
    ans=list(random.sample(l, 4))
    
    
def playAgain():
    print('4A0B')
    print('Congratulation, press anything to continue')
    x=input()
    if x != None:
        print ('猜數字遊戲，請輸入4位數字')
        print ('number=')
        n=list(input())
        ans=random.sample(l, 4)
    return n

      
while n!= ans:
    for i in range(0,4):
            if str(n[i])== str(ans[i]): 
                c=c+1                             
    if c==0:
        print('0A4B')
        print ('再試試看吧:')
        c=0
        n=list(input())
                
                
    elif c==1:
        print('1A3B')
        print ('再試試看吧:')
        c=0
        n=list(input())
                
    elif c==2:
        print('2A2B')
        print ('再試試看吧:')
        c=0
        n=list(input())
                
    elif c==3:
        print('3A1B')
        print ('再試試看吧:')
        c=0
        n=list(input())                
    else:
        c=0
        ans=[]
        playAgain()
        
                       
#! /usr/bin/env python
#coding:utf-8


# Assignment_Team10


print('九九乘法表')

print('\n'.join(['\t'.join(['%d*%d=%d' % (j,i,i*j) for i in range(1,10)]) for j in range(1,10)])) 



#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Assignment_Team14


print ('n SETS OF LOTTERY NUMBERS')
print ('n=')

if __name__ == '__main__':
    import random
    l=range(1,46)
    n=int(input())
    i=1
    while i<=n:
        print(random.sample(l, 6))
        i=i+1          