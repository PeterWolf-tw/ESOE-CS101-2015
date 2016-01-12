#include <cstdlib>
#include <iostream> 
#include <cmath>
using namespace std;



int main(int argc, char *argv[])
{
	double a[1000],sum=0.0,str=0.0;
	int num=0;
	cout<<"input the number of date.\n";
	cin>>num;
	cout<<"input date.\n";
	for(int i=0;i<num;i++)
	{
		cin>>a[i];
		//cout<<a[i]<<endl;
		sum=sum+a[i];
	}
	sum=sum/num;
	for(int i=0;i<num;i++)
	{
		a[i]=a[i]-sum;
		str=str+pow(a[i],2);
	}
	str=str/num;
	cout<<"標準差為"<<sqrt(str);
	system("PAUSE");
    return EXIT_SUCCESS;
}
