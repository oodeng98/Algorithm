#include <stdio.h>

int main(){
	int series;
	scanf("%d",&series);
	int N=0;
	int num=666;
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
		else if(num%1000-num%100==600){
			if(num%10000-num%1000==6000){
				if(num%100000-num%10000==60000){
					N++;
					num++;
					continue;
				}
			}
		}
		else if(num%10000-num%1000==6000){
			if(num%100000-num%10000==60000){
				if(num%1000000-num%100000==600000){
					N++;
					num++;
					continue;
				}
			}
		}
		else if(num%100000-num%10000==60000){
			if(num%1000000-num%100000==600000){
				if(num%10000000-num%1000000==6000000){
					N++;
					num++;
					continue;
				}
			}
		}
		else if(num%1000000-num%100000==600000){
			if(num%10000000-num%1000000==6000000){
				if(num%100000000-num%10000000==60000000){
					N++;
					num++;
					continue;
				}
			}
		}
		else if(num%10000000-num%1000000==6000000){
			if(num%100000000-num%10000000==60000000){
				if(num%1000000000-num%100000000==600000000){
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