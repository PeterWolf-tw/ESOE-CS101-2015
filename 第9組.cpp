#include <cstdlib>
#include <iostream> 
#include <string>
#include <time.h>
using namespace std;
static int c[4];

void make(int c[4]){
	int a=0,t=0;
	srand(time(NULL));
	while(t<4){
		
		a=(rand()%10);
		for(int i=0;i<t;i++){
			if(c[i]==a){
				a=-1;	
			}
		}
		if(a!=-1){
			c[t]=a;
			t++;
		}
	}	
}
void guess(int c[4]){
	int b[4],A=0,B=0;
	do{
		for(int i=0;i<4;i++){
			cin>>b[i];
		}
		for(int i=0;i<4;i++){
			
			if(0==(b[i]-c[0])*(b[i]-c[1])*(b[i]-c[2])*(b[i]-c[3])){
				if(b[i]==c[i])
					A++;
				else
					B++;
			}
		}
		cout<<A<<"A"<<B<<"B\n";
		if(A==4){
			cout<<"Congratulation , press anything to continue !\a\n";
		}
		else{
			cout<<"Try again!\a\n";
			A=0;
			B=0;
		}		
	}while(A!=4);
	cout<<"Input 0 to start new game!\n Or other number to exit!\n";
}

int main(int argc, char *argv[])
{
	int swit=0;
	do{
	make(c);

	for(int i=0;i<4;i++){             //這是答案，交作業前記得註解
		cout<<c[i]<<" ";              //這是答案，交作業前記得註解
	}                                 //這是答案，交作業前記得註解
	cout<<endl;                       //這是答案，交作業前記得註解
	
	guess(c);
	cin>>swit;
	}while(swit==0);
	system("PAUSE");
	return EXIT_SUCCESS;
}
