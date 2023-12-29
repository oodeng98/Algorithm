#include <stdio.h>

int main(){
	int series;
	scanf("%d",&series);
	int N=0;
	int number[6] = {0,0,0,6,6,6};
	int result[10000];
	for(int i=0;i<4;i++){
		if(number[2+i]==6&&number[1+i]==6&&number[i]==6){
			result[N] = number[0]*100000+number[1]*10000+number[2]*1000+number[3]*100+number[4]*10+number[5];
			N++;
			if(N==series){
				printf("%d",result[N-1]);
				break;
			}
			number[5]++;
			for(int i=6;i>0;i--){
				if(number[i]==10){
					number[i-1]++;
					number[i] = 0;
				}
			}
			i=0;
			continue;
		}
		else if(i==3){
			i=0;
			continue;
		}
	}
	return 0;
}