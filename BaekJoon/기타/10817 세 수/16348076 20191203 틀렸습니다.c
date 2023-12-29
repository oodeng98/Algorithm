#include <stdio.h>

int main() {
	int num[3];
	for(int i=0;i<3;i++){
		scanf("%d",&num[i]);
	}
	for(int i=0;i<2;i++){
		if(num[i]>num[i+1]){
			int temp = num[i];
			num[i] = num[i+1];
			num[i+1] = temp;
			i = 0;
			continue;
		}
	}
	for(int i=0;i<3;i++){
		printf("%d",num[i]);
	}
	printf("%d",num[1]);
	return 0;
}
