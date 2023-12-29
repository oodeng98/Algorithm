#include <stdio.h>
int factory(int a){
	if(a==1){
		return 1;
	}
	return a*factory(a-1);
}
int main(){
	int n;
	scanf("%d",&n);
	printf("%d",factory(n));
	return 0;
}