#include<iostream>
using namespace std;
int main(){
	int sum=0;
	int a[7]={1,2,5,8,5,1,1};
	int b[7]={4634347,5663620,4641330,4520954,	
5641333,5808076,4815806};
    for(int i=0;i<7;i++){
    	sum+=a[i]*b[i];
	}
	sum=sum/10;
	cout<<sum;
} 
