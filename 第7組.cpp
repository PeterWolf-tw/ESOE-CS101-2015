#include <cstdlib>
#include <iostream> 
#include <algorithm>
using namespace std;



int main(int argc, char *argv[])
{
	int num=0,s=1,re=0;
	cout<<"input the number of date.\n";
	cin>>num;
	cout<<"input date.\n";
	int a[10],a1[10];
	for(int i=0;i<num;i++)
	{
		cin>>a[i];
		s=s*(i+1);
	}
	cout<<num<<"!="<<s<<endl;
	
	sort(a,a+num); 

	cout<<"\n";
	
	do
	{		
		for(int i=0;i<num;i++)	
		{	
			cout<<a[i]<<" ";
		}	
		cout<<"\n";
	}	while (next_permutation(a,a+num));

	system("PAUSE");
    return EXIT_SUCCESS;
}
