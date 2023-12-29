#include <stdio.h>
int main(){
	int a,b,c;
	scanf("%d",&a);
	scanf("%d",&b);
	scanf("%d",&c);
	if(b>=c){
		printf("-1");
		return 0;
	}
	int i=a/(c-b)+1;
	printf("%d",i);
	return 0;
}

