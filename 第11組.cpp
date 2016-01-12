#include <cstdlib>
#include <iostream> 
#include <time.h>
using namespace std;

void game(int n){
	int pr=0,bomb_num=0,sum=0,start_pr=0,d=1,Input_num=0;
	cout<<"input the number of players.\n";
	cin>>pr;

	char tab[5][21];
	cout<<"Input the name of players.\n";
	for(int i=0;i<pr;i++){//開陣列
		for(int j=0;j<20;j++){//預設成儲存20位
			tab[i][j]='0';
		}
		tab[i][20]='a';//第21位表示 是否能使用功能卡 a代表可以 A代表不行
	}	
	for(int i=0;i<pr;i++){//輸入
		cin>>tab[i];
	}
	for(int k=0;k<pr;k++){//顯示
		for(int l=0;l<20;l++){
			if(tab[k][l]=='0'){
				break;
			}
			else
				cout<<tab[k][l];
		}
	}
	cout<<endl;//開始!
	srand(time(NULL));
	start_pr=(rand()%pr);
	cout<<"Start from ";
	
	for(int j=0;j<20;j++){
		if(tab[start_pr][j]=='0'){
			break;
		}
		else{
			cout<<tab[start_pr][j];
			tab[start_pr][20]='A';
		}
	}
	cout<<endl;
	system("PAUSE");
	bomb_num=(rand()%36)+1;
	cout<<"the bomb number is "<<bomb_num<<endl;
	
	
	for(int i=start_pr+1;i<=pr,i>0;i=i+d){//pr為人數 d代表順序，當有人使用迴轉時 d=d*-1  i的值應為1~pr
		if(sum<bomb_num){
			cout<<"It's ";
			for(int l=0;l<20;l++){
				if(tab[i-1][l]=='0'){
					break;
				}
				else
					cout<<tab[i-1][l];
			}
			cout<<"'s turn!\n";
			if(tab[i-1][20]=='a'){
				cout<<"Input 1,2,3 to increase sum,or 0 to pass -1 to return.\n";
				cin>>Input_num;
				if(Input_num==-1){
					d=d*-1;
					tab[i-1][20]='A';
					cout<<"sum="<<sum<<endl;
				}
				else if(Input_num==0){
					sum+=Input_num;
					tab[i-1][20]='A';
					cout<<"sum="<<sum<<endl;
				}
				else{
					sum+=Input_num;
					cout<<"sum="<<sum<<endl;
				}
			}
			else{
				cout<<"Input 1,2,3 to increase sum.\n";
				cin>>Input_num;
				sum+=Input_num;
				cout<<"sum="<<sum<<endl;
			}
		}
		else{
			cout<<"You lose!.\n";
			break;
		}
		if(i>=pr&&d==1){
			i=0;
		}
		else if(i<=1&&d==-1){
			i=pr+1;
		}
	}
	
	system("PAUSE");
	//return EXIT_SUCCESS;
}
int main(int argc, char *argv[]){
	int a=0;
	do{
		cout<<"Input 0 to start new game.\n";
		cout<<"Input 1 to exit new game.\n";
		cin>>a;
		if(a==0){
			game(0);
		}
	}while(a!=1);

}