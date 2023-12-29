#include <stdio.h>

int main(){
	int var;
	scanf("%d",&var);
	int score[1000];
	int max = 0;
	float total = 0;
	for(int i=0;i<var;i++){
		scanf("%d",&score[i]);
		if(max<score[i]){
			max = score[i];
		}
		total+=score[i];
	}
	printf("%.2lf",(total/var)*100/(max));
	return 0;
}
