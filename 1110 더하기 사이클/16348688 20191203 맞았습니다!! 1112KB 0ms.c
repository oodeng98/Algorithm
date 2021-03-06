#include <stdio.h>

int main() {
	int a;
	scanf("%d",&a);
	int b;
	int count = 0;
	if(a<10){
		a = a*10;
	}
	b = a;
	while(1){
		b = b%10*10+(b/10+b%10)%10;
		count++;
		if(a==b){
			break;
		}
	}
	printf("%d",count);
	return 0;
}
