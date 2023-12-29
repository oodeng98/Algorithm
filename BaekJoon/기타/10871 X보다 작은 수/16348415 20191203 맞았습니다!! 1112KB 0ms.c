#include <stdio.h>

int main() {
	int n,x;
	scanf("%d",&n);
	scanf("%d",&x);
	int num[10000];
	for(int i=0;i<n;i++){
		scanf("%d",&num[i]);
	}
	for(int i=0;i<n;i++){
		if(num[i]<x){
			printf("%d ",num[i]);
		}
	}
	return 0;
}
