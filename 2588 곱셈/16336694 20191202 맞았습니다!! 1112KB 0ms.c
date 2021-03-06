#include <stdio.h>

int main() {
	int a,b;
	scanf("%d",&a);
	scanf("%d",&b);
	printf("%d\n",a*(b%10));
	printf("%d\n",a*(b%100-b%10)/10);
	printf("%d\n",a*(b/100));
	printf("%d",a*b);
	return 0;
}
