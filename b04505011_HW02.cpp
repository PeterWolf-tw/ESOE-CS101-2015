#include <cstdlib>
#include <iostream> 
#include <math.h>
using namespace std;

int main(int argc, char *argv[])
{
    string str1;
	int i,j;
	int sum=0;
	cout<<"輸入二進位的數!\n";
	cin>>str1;
	i=str1.size();
	
	//cout<<"i="<<i<<"\n";
	for(j=0;j<i;j++)
	{	
		if(str1[j]>49||str1[j]<48)
		{
		 cout<<"格式錯誤!\n";
		 j=-2;
		 break;
		}
		else
		{
		 //cout<<str1[j]<<"\n";	
		 sum+=(str1[j]-48)*pow(2,i-1-j);
		}
	}
    if(j!=-2)
	{
	 cout<<"它的十進位表示法為"<<sum<<"\n";
    }
	
	/*  p2-19.
			  a.2^9=512<1000<2^10=1024 故答案取9+1=10
			  b.答案取16+1=17
			  c.64=2^6 答案取6
			  d.答案取8
		p2-20.
			  a.答案=14
			  b.答案=8
			  c.答案=13
			  d.答案=4
		p2-22.
			  a.00010001 11101010 00100010 00001110
			  b.00001110 00111000 11101010 00111000
			  c.01101110 00001110 00111000 01001110
			  d.00011000 00111000 00001101 00001011
		p3-28. 
			  a.765
			  b.439
			  c.125
			  d.111
		p3-30.
			  a.766
			  b.440			  
			  c.125
	          d.111*/
	
	
	
	system("PAUSE");
    return EXIT_SUCCESS;
}
