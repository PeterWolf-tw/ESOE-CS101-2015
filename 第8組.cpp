#include <cstdlib>
#include <iostream>

using namespace std;
	int inpt=0, exp[3][3]={1,2,3,
					 4,5,6,
					 7,8,9};
	char gam[3][3]={'1','2','3',				 
					 '4','5','6',				 
					 '7','8','9'};		

void outpt(int i=0,int j=0){
	
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			cout<<gam[i][j]<<"\t";
		}
		cout<<endl<<"\n";
	}
}
int inspect(char gam[3][3]){
	int qq=0;
	if(gam[0][0]==gam[1][0]&&gam[1][0]==gam[2][0]){
		qq--;
	}
	else if(gam[0][1]==gam[1][1]&&gam[1][1]==gam[2][1]){
		qq--;
	}
	else if(gam[0][2]==gam[1][2]&&gam[1][2]==gam[2][2]){
		qq--;
	}
	else if(gam[0][0]==gam[0][1]&&gam[0][1]==gam[0][2]){
		qq--;
	}
	else if(gam[1][0]==gam[1][1]&&gam[1][1]==gam[1][2]){
		qq--;
	}
	else if(gam[2][0]==gam[2][1]&&gam[2][1]==gam[2][2]){
		qq--;
	}
	else if(gam[0][0]==gam[1][1]&&gam[1][1]==gam[2][2]){
		qq--;
	}
	else if(gam[0][2]==gam[1][1]&&gam[1][1]==gam[2][0]){
		qq--;
	}
	else{
		qq=1;
	}
	return qq;
}
int main(int argc, char *argv[]){		 
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			cout<<exp[i][j]<<"\t";
		}
		cout<<endl<<"\n";
	}
	cout<<endl<<"Please input numbers to select the relative part.\n";
	
	for(int i=0;i<100;i++){
		if(i%2==0){
			cout<<"Player1:";
			cin>>inpt;
			inpt--;
			gam[inpt/3][inpt%3]='O';
			outpt(0,0);
		}
		else if(i%2==1){
			cout<<"Player2:";
			cin>>inpt;
			inpt--;
			gam[inpt/3][inpt%3]='X';
			outpt(0,0);
		}
		i=i*inspect(gam);
		if(i<0){
			i=i*-1;
			if(i%2==0)
				cout<<"Player1 Win!\n";
			else
				cout<<"Player2 Win!\n";
			break;
		}
	}
	
	cout<<"\ngame over!\n";
	
	
	
	
	
	system("PAUSE");
	return EXIT_SUCCESS;
}
