#include <stdio.h>
int main(){
	int kg;
	scanf("%d",&kg);
	for(int i=0;i<1700;i++){
		for(int j=0;j<1001;j++){
			if(3*i+5*j==kg){
				printf("%d",i+j);
				return 0;
			}
		}
	}
	printf("-1");
	return 0;
}

