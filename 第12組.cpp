#include <cstdlib>
#include <iostream>
#include <cmath>
using namespace std;

int main(int argc, char *argv[]){
/* 	int am = 4;
	cout << (char)(am + 'a'); */
	int m=0,n=0,inpt=0,dec=0,tran=0;
	string str1;
	int a[20];
	
	cout<<"m=";
	cin>>m;
	cout<<"n=";
	cin>>n;
	cout<<"Input string:";
	cin>>str1;
	for(int i=0;i<str1.size();i++){
		inpt=str1[i]-0;
		
		if(inpt<58){
			inpt=inpt-48;
		}
		else if(inpt<91){
			inpt=inpt-55;
		}
		else {
			inpt=inpt-61;
		}
		if(inpt>=m){
			cout<<"Error!\n";
			dec++;
			dec*=-1;
			break;
		}
		else{
			dec+=inpt*pow(m,str1.size()-i-1);
		}
	}
	cout<<"dec="<<dec<<endl;
	if(dec<0){
		cout<<"\a";
	}
	else{
		int cnt=0;
		do{
			tran=dec%n;
			dec=dec/n;
			a[cnt]=tran;
			cnt++;
			//cout<<tran<<endl;
		}while(dec>n);
		
		tran=dec%n;
		dec=dec/n;
		a[cnt]=tran;
		cnt++;
		//cout<<tran<<endl;
		//cout<<endl<<dec<<"\t";
		if(dec<10){
			cout<<dec<<"\t";
		}
		else if(dec>9&&dec<36){
			cout<<(char)(dec-10+ 'A')<<"\t";
		}
		else{
			cout<<(char)(dec-35+ 'a')<<"\t";
		}
		for(int i=cnt-1;i>-1;i--){
			//cout<<a[i]<<"\t";
			if(a[i]<10){
		    	cout<<a[i]<<"\t";
		    }
		    else if(a[i]>9&&a[i]<36){
		    	cout<<(char)(a[i]-10+ 'A')<<"\t";
		    }
		    else{
		    	cout<<(char)(a[i]-35+ 'a')<<"\t";
		    }
		}
		cout<<"\nend!\n";
	}
	system("PAUSE");
    return EXIT_SUCCESS;
}

//0=48,A=65 A=10,a=97 a=36    cout << (char)(tran + 'a')<<endl;
