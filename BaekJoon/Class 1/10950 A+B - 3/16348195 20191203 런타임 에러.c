#include <stdio.h>

int main() {
	int n;
	scanf("%d",&n);
	int num[100];
	for(int i=0;i<n;i++){
		scanf("%d",&num[2*i]);
		scanf("%d",&num[2*i+1]);
	}
	for(int i=0;i<n;i++){
		printf("%d\n",num[2*i]+num[2*i+1]);
	}
	return 0;
}
