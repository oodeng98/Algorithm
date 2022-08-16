#include <stdio.h>

int main() {
	int n;
	int a,b;
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		scanf("%d",&a);
		scanf("%d",&b);
		printf("Case #%d: %d + %d = %d\n",i+1,a,b,a+b);
	}
	return 0;
}
