#include <stdio.h>

int main() {
	int a,b;
	while(1){
		scanf("%d",&a);
		scanf("%d",&b);
		printf("%d\n",a+b);
		if(a==0&&b==0){
			break;
		}
	}
	return 0;
}
