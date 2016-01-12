#include <cstdlib>
#include <iostream> 

using namespace std;
int f(int n=0){
	if(n==1)
	return 1;
	else if(n==2)
	return 1;
	else{
		return f(n-1)+f(n-2);
	}
}
int main(int argc, char *argv[]){
	int a=0;
	cout<<"費氏數列的第幾項?\n";
	cin>>a;
	cout<<f(a)<<endl;
	system("PAUSE");
	return EXIT_SUCCESS;
}