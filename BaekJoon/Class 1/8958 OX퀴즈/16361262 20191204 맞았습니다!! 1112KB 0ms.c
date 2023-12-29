#include <stdio.h>

int main(){
	int var;
	scanf("%d",&var);

	for(int i=0;i<var;i++){
		char test[80];
		scanf("%s",test);
		int total=0;
		int size;
		int score=0;
		for(int i=0;i<80;i++){
			if(test[i]==NULL){
				size = i+1;
				break;
			}
		}
		for(int i=0;i<size-1;i++){
			if(test[i]=='O'){
				score++;
				total += score;
			}
			else if(test[i]=='X'){
				score = 0;
			}
		}
		printf("%d\n",total);
	}

	return 0;
}
