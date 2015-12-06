#include<iostream>
#include<cstdlib>
char input[100];
int freq[128] = {0};
bool freqL[128][101] = {false};
int count = 0;
void charFreqLister(){
    for(int i=0;;i++){
        if(input[i] == '\0')  break;
        freq[input[i]]++;
        count++;
        }
    for(int i=0;i<128;i++){
        if(!freq[i])  continue;
        freqL[i][freq[i]] = true;
        } 
    }
int main(){
    std::cin.getline(input,100);
    charFreqLister();
    for(int j=100;j>0;j--){
        for(int i=0;i<128;i++){
            if(freqL[i][j]){
                std::cout<<(char)i<<" "<<j<<" "<<(float)j/(float)count<<"\n";
                }
            }
        }
    system("pause");
    return 0;
    }
