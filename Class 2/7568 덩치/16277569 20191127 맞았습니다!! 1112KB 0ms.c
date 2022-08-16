#include <stdio.h>
typedef struct{
	int height;
	int weight;
	int score;
} info;

int main(){
	int total;
	scanf("%d",&total);
	info people[50];
	for(int i=0;i<total;i++){
		scanf("%d",&people[i].weight);
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