#include <stdio.h>
int main(){
	int n;
	scanf("%d",&n);
	if(n==1){
		printf("1");
		return 0;
	}
	else if(n<8){
		printf("2");
		return 0;
	}
	int count = 2;
	int len[19000];
	len[0] = 1;
	for(int i=1;i<19000;i++){
		len[i] = len[i-1]+i+1;
	}
	for(int i=0;i<19000;i++){
		if(2+6*len[i]<n){
			count++;
		}
		else{
			break;
		}
	}
	printf("%d",count);
	return 0;
}
