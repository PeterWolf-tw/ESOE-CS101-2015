#include <cstdlib>
#include <iostream>
using namespace std;

int main(int argc, char *argv[]){
	for(int i=1;i<10;i++){
		for(int j=1;j<10;j++){
			if(i*j<10){
				cout<<"0"<<i*j<<"\t";
			}
			else{
				cout<<i*j<<"\t";
			}
		}cout<<endl;
	}
	system("PAUSE");
	return EXIT_SUCCESS;
}