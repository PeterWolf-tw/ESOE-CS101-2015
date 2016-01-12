#include <cstdlib>
#include <iostream> 
#include <algorithm>
#include <time.h>
using namespace std;

int main(int argc, char *argv[])
{
	int a=0,b=0,c[6];
	srand(time(NULL));
	int t=0;
	cin>>b;
	for(int j=0;j<b;j++){
		
		while(t<6){
			
			a=(rand()%49)+1;
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
		for(int i=0;i<6;i++){
				sort(c,c+6);
				cout<<c[i]<<" ";
				if(i==5)
				cout<<"\n";
			}
		t=0;
	}
	
	
	
	
	
	system("PAUSE");
	return EXIT_SUCCESS;
}