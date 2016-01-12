#include <cstdlib>
#include <iostream> 
#include <string>
using namespace std;



int main(int argc, char *argv[])
{
	cout<<"Input a word in English.\n";
	string str1,str2;
	cin>>str1;
	int q=0;
	q=str1.size();
	for(int i=0;i<q;i++){
		if(str1[i]=='0'||str1[i]=='1'||str1[i]=='2'||str1[i]=='3'||str1[i]=='4'||str1[i]=='5'||str1[i]=='6'||str1[i]=='7'||str1[i]=='8'||str1[i]=='9'){
				cout<<"Error!\n";
				break;
		}
		else if(i>0){
			str2=str1[i];
			cout<<str2;
		}
		if(i==q-1){
			cout<<str1[0]<<"ay\n";
		}
	}
		
	
	
	system("PAUSE");
    return EXIT_SUCCESS;
}
