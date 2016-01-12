#include <cstdlib>
#include <iostream>
using namespace std;

int main(int argc, char *argv[]){
	string A,B;
	int a,b;
	getline(cin,A);
	cout<<"\n";
	switch(A[1]){
		case 'd'://3
		a=60;
		break;
		case 'r'://4
		a=4;
		break;
		case 'y'://5
		a=-6;
		break;
		case 'o':
		if(A[0]=='J'){//1
			a=3;
		}
		else if(A[0]=='R'){//2
			a=15;
		}
		else{
			a=2;//9
		}
		break;
		case 'a'://6
		a=-12;
		break;
		case 'h'://7
		a=0;
		break;
		case 'e'://8
		a=5;
		break;
		default:
		a=0;
		break;
	}
	getline(cin,B);
	switch(B[1]){
		case 'd'://3
		b=60;
		break;
		case 'r'://4
		b=4;
		break;
		case 'y'://5
		b=-6;
		break;
		case 'o':
		if(B[0]=='J'){//1
			b=3;
		}
		else if(B[0]=='R'){//2
			b=15;
		}
		else{
			b=2;//9
		}
		break;
		case 'a'://6
		b=-12;
		break;
		case 'h'://7
		b=0;
		break;
		case 'e'://8
		b=5;
		break;
		default:
		b=0;
		break;
	}

	if(a*b==0){
		cout<<"error";
	}
	else if(a*b<0){
		cout<<"A is B's enemy.";
	}
	else{
		if(a>b){
			cout<<A<<" is "<<B<<"'s senior officer.\n";
		}
		else{
			cout<<A<<" is "<<B<<"'s subordinate. \n";
		}
	}
	system("PAUSE");
	return EXIT_SUCCESS;
}

