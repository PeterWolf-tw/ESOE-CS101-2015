#include <cstdlib>
#include <iostream> 
#include <cmath>

using namespace std;
int main(int argc, char *argv[]){
	float x[20],y[20];
	double x_a=0.0,y_a=0.0,num=0.0,t1=0.0,t2=0.0,xbar=0.0,ybar=0.0;
	double  m=0.0;
	cout<<"Input the number of data.\n";
	cin>>num;
	cout<<"Input xdata.\n";
	for(int i=0;i<num;i++){
		cin>>x[i];
		x_a=x_a+x[i];
	}
	cout<<"Input ydata.\n";
	for(int i=0;i<num;i++){
		cin>>y[i];
		y_a=y_a+y[i];
	}
	x_a=x_a/num;
	y_a=y_a/num;
	for(int i=0;i<num;i++){
		t1=x[i]-x_a;
		t2=y[i]-y_a;
		m=m+t1*t2;
		ybar+=pow(t2,2);
	}
	m=m/ybar;
	xbar=m*x_a;
	xbar=y_a-xbar;
	cout<<"y="<<m<<"x+"<<xbar<<endl;
	system("PAUSE");
	return EXIT_SUCCESS;
}