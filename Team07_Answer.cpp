/*
# ===== Team07 =====
# Team01: Pass
# Team02: Fail : 放棄作答
# Team03: Pass 
# Team04: Fail : 沒有主程式，無法輸入。
# Team05: Pass 
# Team06: Fail : 放棄作答
# Team08: Fail : 放棄作答
# Team09: Fail : 沒有主程式，無法輸入。
# Team10:  --  : 你們的檔案勒QAQ
# Team11: Fail : 沒有主程式，無法輸入。
# Team12: Pass 
# Team13: Pass
# Team14: Fail : 放棄作答

-----------我是分隔線-----------

本題所使用的演算法為回溯法(backtracking)
算是廣義上的一種窮舉法
可以想像為在求出所有排列可能時用的樹狀圖法
而該演算法在窮舉過程中也使用了遞迴的技巧
另外 也可以直接使用next_permutation()等函式
在python中也存在類似的函式

*/
#include <iostream>
#define N 1000
using namespace std;
int ans[N] = {0};
bool used[N] = {0};
int input[N] ={0};
int c = 0;
int num = 0;
void print(){
    for(int i=0;i<num;i++){
        cout<<ans[i]<<" ";
    }
    cout<<'\n';
}
void backtrack(int n){ //回溯法函式
    if(n == num){
        print();
        c++;
        return ;
    }
    for (int i=0; i<num; i++)
        if (!used[i])
        {
            used[i] = true;
            ans[n] = input[i];
            backtrack(n+1); //遞迴至下一層
            used[i] = false;
        }
    }
int main()
{
    cin>>num;
    for(int i=0;i<num;i++){
        cin>>input[i];
    }
    backtrack(0);
    cout<<c<<'\n';
    return 0;
}