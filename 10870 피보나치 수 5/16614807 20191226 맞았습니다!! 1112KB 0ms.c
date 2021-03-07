#include <stdio.h>
int Fibonacci(int a){
	if(a==0){
		return 0;
	}
	else if(a==1){
		return 1;
	}
	return Fibonacci(a-1)+Fibonacci(a-2);
}
int main(){
	int n;
	scanf("%d",&n);
	printf("%d",Fibonacci(n));
	return 0;
}