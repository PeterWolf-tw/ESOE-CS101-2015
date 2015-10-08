#include<iostream>
#include<math.h>
int btd(std::string s){
	int d = 0, n = s.length();
	for(int i = 0 ; i < n ; i++)	d += ((s[i]-48)*pow(2,n-1-i));
	return d;
}
int main(){
	std::string input;
	std::cout<<"Please enter a binary number : \n";
	while(std::cin >> input)	std::cout<<btd(input)<<"\n";
	return 0;
}
