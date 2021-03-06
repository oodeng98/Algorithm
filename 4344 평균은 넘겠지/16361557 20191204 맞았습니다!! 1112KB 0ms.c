#include <stdio.h>

int main(){
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		int score[1000];
		int stu=0;
		float over = 0;
		float total=0;
		scanf("%d",&stu);
		for(int j=0;j<stu;j++){
			scanf("%d",&score[j]);
			total+=score[j];
		}
		for(int j=0;j<stu;j++){
			if(total/stu<score[j]){
				over++;
			}
		}
		printf("%.3lf%\n",(over/stu)*100);
	}
	return 0;
}
