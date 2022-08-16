#include <stdio.h>

int main() {
	int a;
	scanf("%d",&a);
	if(a>=90&&a<=100){
		printf("A");
	}
	else if(a<90&&a>=80){
		printf("B");
	}
	else if(a<80&&a>=70){
		printf("C");
	}
	else
		printf("F");
	return 0;
}
