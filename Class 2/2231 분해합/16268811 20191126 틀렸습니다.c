#include <stdio.h>

int main(){
	int num;
	scanf("%d",&num);
	if(num<=10){
		printf("0");
		return 0;
	}
	for(int i=0;i<num;i++){
		if((i+i/1000000+i%1000000/100000+i%100000/10000+i%10000/1000+i%1000/100+i%100/10+i%10)==num){
			printf("%d",i);
			break;
		}
		else if(i==num-1){
			printf("0");
			break;
		}
	}
	return 0;
}