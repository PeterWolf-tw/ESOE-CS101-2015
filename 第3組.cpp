#include <cstdlib>
#include <iostream>
using namespace std;

int main(int argc, char *argv[]){
	char fri1[3][3]={'a','b','c',
					 'b','a','a',
					 'c',' ',' '};
	char fri2[4][4]={'1','2','3','4',
					 '2','1','1','2',
					 '3','4',' ',' ',
					 ' ',' ',' ',' '};
	cout<<"friends1.name:";
	for(int i=0;i<3;i++){
		cout<<fri1[0][i];
		if(i==2){
			cout<<endl;
			break;
		}
		cout<<',';
	}
	cout<<"friends1.connected('d') == ";
	for(int i=0;i<3;i++){
		if('d'==fri1[0][i]){
			for(int j=1;j<3;j++){
				cout<<fri1[i][j];
			}
		}
	}
	cout<<"\nfriends1.connected('a') == ";
	for(int i=0;i<3;i++){
		if('a'==fri1[0][i]){
			for(int j=1;j<3;j++){
				cout<<fri1[i][j];
			}
		}
	}
	cout<<endl;	
	cout<<"friends2.name:";
	for(int i=0;i<4;i++){
		cout<<fri2[0][i];
		if(i==3){
			cout<<endl;
			break;
		}
		cout<<',';
	}
	cout<<"friends2.connected('1') == ";
	for(int i=0;i<4;i++){
		if('1'==fri2[0][i]){
			for(int j=1;j<4;j++){
				cout<<fri2[i][j];
			}
		}
	}
	cout<<endl;	
	system("PAUSE");
	return EXIT_SUCCESS;	
}//我還不太會用class裡面的函式，所以暫時先按照題目要求print結果