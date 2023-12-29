#include <stdio.h>
int main(){
	int N;
	scanf("%d",&N);
	if(N==1000){
		printf("144");
	}
	else if(N<100){
		printf("%d",N);
	}
	else{
		int count = 99;
		for(int i=100;i<N+1;i++){
			if(i/100+i%10==(i%100-i%10)/5){
				count++;
			}
		}
		printf("%d",count);
	}
	return 0;
}

