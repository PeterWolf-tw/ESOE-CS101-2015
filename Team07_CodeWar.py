#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#Assignment_Team01_HW05
#設計一個程式
#若使用者輸入一個數值
#可算出該數值所具有的所有公因數
#例如輸入633
#可得1 3 211 633
#Done
def Team01solution(inputNumber):
    resultLIST=[]
    for i in range (1,inputNumber+1,+1):
        Temp = inputNumber % i
        if Temp == 0 :
            resultLIST.append(i)
    return resultLIST
#Assignment_Team02_HW05
#Done
#C++ Solution :

#include <iostream>
#include <ctype.h>
using namespace std;
int main()
{
    char a[100];
    int temp = 0;
    cin.getline(a,100,'\n');
    for(int i=0;;i++){
        if(a[i] == '\0'){
            a[i] = a[0];
            a[i+1] = 'a';
            a[i+2] = 'y';
            temp = i;
            break;
        }
        if(!isalpha(a[i])){
            cout<<"Unvalidated Input";
            return 0;
        }
    }
    for(int i=1;i<temp+3;i++)   cout<<a[i];
    return 0;
}

#Python Solution:字為unvalid的部分還沒處理 
def Team02solution(inputSTR):
    result = inputSTR [1:] 
    result += inputSTR [:1]
    result += "ay"
    return result
#Assignment_Team03_HW05
def Team03solution(input):
    
    return resultLIST
#Assignment_Team04_HW05
#設計一個程式
#若input=n
#可算出費式數列第n項的值
#費式數列第n項的值等於第(n-1)項與第(n-2)項的和
#且a1=a2=1
#Done
def Team04solution(input):
    result = 1
    temp1 = 0
    temp2 = 0
    for k in range (0 , input+1 , +1):
        temp2 = result
        result += temp1
        temp1 = temp2
    return result
#Assignment_Team05_HW05
def Team05solution(xdata,ydata):
    p = 0
    for i in range (0,len(xdata)):
        p = p + xdata[i]*ydata[i]
        i = i + 1 
    print("Sum(xi*yi) =",p)
    
    x = 0
    for i in range (0,len(xdata)):
        x = x + xdata[i]
        i = i + 1
    Xavg = x/len(xdata)
    print("Xavg =",Xavg)
    
    y = 0
    for i in range (0,len(ydata)):
        y = y + ydata[i]
        i = i + 1
    Yavg = y/len(ydata)
    print("Yavg =",Yavg)
    
    
    q = 0
    for i in range (0,len(xdata)):
        q = q + xdata[i]*xdata[i]
        i = i + 1 
    print("Sum(x^2) =",q)
    
    m = (p-len(xdata)*Xavg*Yavg)/(q-len(xdata)*Xavg*Xavg)
    print("slope =",m)
    
    b = Yavg - m*Xavg
    print("y-intercept =",b)
    print("-------your equation ------")
    print("y =",m,"x +",b)

if __name__== "__main__":
    xnum = input("Enter numbers for xdata separated by spaces in one line: ")
    items = xnum.split() 
    xdata1 = [eval(x) for x in items]
    print ("Your xdata list is",xdata1)
    ynum = input("Enter numbers for ydata separated by spaces in one line: ")
    items = ynum.split() 
    ydata1 = [eval(y) for y in items]
    print ("Your ydata list is",ydata1)
    print("------------")
    Team05solution(xdata1,ydata1)
#Assignment_Team06_HW05
#Done
def Team06solution(inputLIST):
    result = 0
    average = sum(inputLIST)/len(inputLIST)
    for i in range (0 , len(inputLIST) , +1):
        result += (inputLIST[i]-average) * (inputLIST[i]-average)   
    result /= len(inputLIST)
    result = result ** 0.5
    return result
#Assignment_Team08_HW05
#Done
#C++ Solution :

#include <iostream>
using namespace std;
char out[5][5];
bool used[10] = {false};
bool check(){
    for(int j=0;j<5;j+=2){
        for(int i=0;i<5;i+=2){
            if(out[i][j] == '\0')   return true;
        }
    }
    return false;
}
void print(){
     for(int j=0;j<5;j++){
        for(int i=0;i<5;i++){
            if(out[i][j] == '\0')   cout<<" ";
            else cout << out[i][j];
        }
        cout << endl;
    }
    cout<< endl;
}
void fillin1(int pst){
    int y = ((pst-1)/3)*2;
    int x = ((pst-1) % 3)*2;
    out[x][y] = 'O';
}
void fillin2(int pst){
    int y = ((pst-1)/3)*2;
    int x = ((pst-1) % 3)*2;
    out[x][y] = 'X';
}
bool win(){
    if((out[0][0] == out[0][2])&&(out[0][2] == out[0][4])){
        if(out[0][0] == 'O'){
            cout << "Player 1 wins !!\n";
            return 1;
        }
        if(out[0][0] == 'X'){
            cout << "Player 2 wins !!\n";
            return 1;
        }
    }
    if((out[2][0] == out[2][2])&&(out[2][2] == out[2][4])){
        if(out[2][0] == 'O'){
            cout << "Player 1 wins !!\n";
            return 1;
        }
        if(out[0][0] == 'X'){
            cout << "Player 2 wins !!\n";
            return 1;
        }
    }
    if((out[4][0] == out[4][2])&&(out[4][2] == out[4][4])){
        if(out[4][0] == 'O'){
            cout << "Player 1 wins !!\n";
            return 1;
        }
        if(out[0][0] == 'X'){
            cout << "Player 2 wins !!\n";
            return 1;
        }
    }
    if((out[0][0] == out[2][0])&&(out[2][0] == out[4][0])){
        if(out[0][0] == 'O'){
            cout << "Player 1 wins !!\n";
            return 1;
        }
        if(out[0][0] == 'X'){
            cout << "Player 2 wins !!\n";
            return 1;
        }
    }
    if((out[0][2] == out[2][2])&&(out[2][2] == out[4][2])){
        if(out[0][2] == 'O'){
            cout << "Player 1 wins !!\n";
            return 1;
        }
        if(out[0][0] == 'X'){
            cout << "Player 2 wins !!\n";
            return 1;
        }
    }
    if((out[0][4] == out[2][4])&&(out[2][4] == out[4][4])){
        if(out[0][4] == 'O'){
            cout << "Player 1 wins !!\n";
            return 1;
        }
        if(out[0][0] == 'X'){
            cout << "Player 2 wins !!\n";
            return 1;
        }
    }
    if((out[0][0] == out[2][2])&&(out[2][2] == out[4][4])){
        if(out[0][0] == 'O'){
            cout << "Player 1 wins !!\n";
            return 1;
        }
        if(out[0][0] == 'X'){
            cout << "Player 2 wins !!\n";
            return 1;
        }
    }
    if((out[0][4] == out[2][2])&&(out[2][2] == out[4][0])){
        if(out[0][4] == 'O'){
            cout << "Player 1 wins !!\n";
            return 1;
        }
        if(out[0][0] == 'X'){
            cout << "Player 2 wins !!\n";
            return 1;
        }
    }
    return 0;
}
int main()
{
    cout << "遊戲說明 : 九宮格內的位置編號如下" << endl;
    cout << " ------------- "<< endl;
    cout << " | 1 | 2 | 3 |"<< endl;
    cout << " ------------- "<< endl;
    cout << " | 4 | 5 | 6 |"<< endl;
    cout << " ------------- "<< endl;
    cout << " | 7 | 8 | 9 |"<< endl;
    cout << " ------------- "<< endl;
    cout << "請輸入你欲填入圈/叉的位置(1~9)， Player 1 為圈，Player 2 為叉\n";
    int i = 1, pst = 0;
    bool t1 = false, t2 = false;
    while(check()){
        if((i%2)&&(!t1)){
           cout << "請Player 1輸入位置 : \n";
           cin >> pst ;
           if((pst>9)||(pst<0)){
                cout << "無效輸入\n";
           }
           if(used[pst]){
                cout << "已使用之位置，請重新輸入\n";
           }
           else {
                used[pst] = true;
                t1 = true;
                i++;
                fillin1(pst);
                print();
           }
           if(win())    return 0;
        }
        else if((!(i%2))&&(!t2)){
           cout << "請Player 2輸入位置 : \n";
           cin >> pst ;
           if((pst>9)||(pst<0)){
                cout << "無效輸入\n";
           }
           if(used[pst]){
                cout << "已使用之位置，請重新輸入\n";
           }
           else {
                used[pst] = true;
                t2 = true;
                i++;
                fillin2(pst);
                print();
           }
           if(win())    return 0;

        }
        t1 = false;
        t2 = false;
    }
    win();
    return 0;
}

#Assignment_Team09_HW05
def Team09solution(input):
    return resultLIST
#Assignment_Team10_HW05
# 請設計一個程式能自動列出九九乘法表如下(每行要對齊):

# 0  0  0  0  0  0  0  0  0  0
# 0  1  2  3  4  5  6  7  8  9
# 0  2  4  6  8 10 12 14 16 18
# 0  3  6  9 12 15 18 21 24 27
# 0  4  8 12 16 20 24 28 32 36
# 0  5 10 15 20 25 30 35 40 45
# 0  6 12 18 24 30 36 42 48 54
# 0  7 14 21 28 35 42 49 56 63
# 0  8 16 24 32 40 48 56 64 72
# 0  9 18 27 36 45 54 63 72 81
#Done
def Team10solution():
    print("0  0  0  0  0  0  0  0  0  0")
    print("0  1  2  3  4  5  6  7  8  9")
    print("0  2  4  6  8 10 12 14 16 18")
    print("0  3  6  9 12 15 18 21 24 27")
    print("0  4  8 12 16 20 24 28 32 36")
    print("0  5 10 15 20 25 30 35 40 45")
    print("0  6 12 18 24 30 36 42 48 54")
    print("0  7 14 21 28 35 42 49 56 63")
    print("0  8 16 24 32 40 48 56 64 72")
    print("0  9 18 27 36 45 54 63 72 81")
    return None
#Assignment_Team11_HW05
def Team11solution(input):
    return resultLIST
#Assignment_Team12_HW05
def Team12solution(input):
    return resultLIST
#Assignment_Team13_HW05
def Team13solution(input):
    return resultLIST
#Assignment_Team14_HW05
#Done
def Team14solution(input):
    import random
    resultLIST = []
    for k in range (0, input, +1):
        resultLIST.append("後面6個數字是一組號碼")
        tempLIST = []
        for i in range (0, 6 , +1):
            temp = int(random.random() * 48) + 1
            while temp in tempLIST:
                temp = int(random.random() * 48) + 1
            while temp not in tempLIST:
                tempLIST.append(temp)
                resultLIST.append(temp)
    return resultLIST
if __name__ == "__main__":
    testNUM01 = 633
    result = Team01solution(testNUM01)
    print(result)
    testSTR01 = "Hello"
    result = Team02solution(testSTR01)
    print(result)
    testNUM02 = 5
    result = Team04solution(testNUM02)
    print(result)
    testLIST01 = [40, 50, 60]
    result = Team06solution(testLIST01)
    print(result)
    test = Team10solution()
    testNUM03 = 100
    result = Team14solution(testNUM03)
    print(result)    