#include <stdio.h>
typedef struct{
	int height;
	int weight;
	int score;
} info;

int main(){
	printf("전체 사람의 수를 입력해주세요: ");
	int total;//전체 사람 수
	scanf("%d",&total);
	info people[50];
	for(int i=0;i<total;i++){
		printf("%d번째 사람의 몸무게를 입력해주세요: ",i+1);
		scanf("%d",&people[i].weight);
		printf("%d번째 사람의 키를 입력해주세요: ",i+1);
		scanf("%d",&people[i].height);
		people[i].score = 1;
	}
	for(int i=0;i<total;i++){
		for(int j=0;j<total;j++){
			if(people[i].height<people[j].height&&people[i].weight<people[j].weight){
				people[i].score++;
			}
		}
	}
	for(int i=0;i<total;i++){
		printf("%d ",people[i].score);
	}
	return 0;
}