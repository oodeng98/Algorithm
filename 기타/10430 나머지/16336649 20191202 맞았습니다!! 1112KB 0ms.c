#include <stdio.h>

int main() {
	int a,b,c;
	scanf("%d",&a);
	scanf("%d",&b);
	scanf("%d",&c);
	printf("%d\n",(a+b)%c);
	printf("%d\n",(a%c+b%c)%c);
	printf("%d\n",(a*b)%c);
	printf("%d\n",((a%c)*(b%c))%c);
	return 0;
}
