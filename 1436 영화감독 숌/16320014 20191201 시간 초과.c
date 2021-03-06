#include <stdio.h>

int main(){
	int series;
	scanf("%d",&series);
	int N=0;
	int num=666;
	int number[10];
	while(N!=series){
		if(num%10==6){
			if(num%100-num%10==60){
				if(num%1000-num%100==600){
					N++;
					num++;
					continue;
				}
			}
		}
		else if(num%100-num%10==60){
			if(num%1000-num%100==600){
				if(num%10000-num%1000==6000){
					N++;
					num++;
					continue;
				}
			}
		}
		else{
			num++;
		}
	}
	printf("%d",num-1);
	return 0;
}