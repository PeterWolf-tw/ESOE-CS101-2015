#include <cstdlib>
#include <iostream> 
#include <string>
#include <cmath>
using namespace std;



int main(int argc, char *argv[])
{
	cout<<"Input a number!\n";
	int num=0;
	cin>>num;
	
	for(int i=1;i<=num;i++)
	{
		if(num%i==0)
		{
			cout<<i<<" "<<-i;
			if(num!=i)
			cout<<" ";
		}
	}
	system("PAUSE");
    return EXIT_SUCCESS;
}
