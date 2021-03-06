#include <stdio.h>

int main(){
	int n,m;
	int card[100];
	printf("몇장의 카드를 공개할 것인지 선택해주세요: ");
	scanf("%d",&n);
	printf("원하는 숫자를 입력해주세요: ");
	scanf("%d",&m);
	for(int i=0;i<n;i++){
		printf("공개된 카드의 숫자를 입력해주세요: ");
		scanf("%d",&card[i]);
	}
	int goal = 0;
	for(int i=0;i<n-2;i++){
		for(int j=i+1;j<n-1;j++){
			for(int k=j+1;k<n;k++){
				if((card[i]+card[j]+card[k]>goal)&&(card[i]+card[j]+card[k]<=m)){
					goal = card[i]+card[j]+card[k];
				}
			}
		}
	}
	printf("%d",goal);
	return 0;
}