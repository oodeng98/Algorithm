#include <stdio.h>
int main(){
	int low,high;
	scanf("%d",&low);
	scanf("%d",&high);
	if(low==1){
		low = 2;
	}
	for(int i=low;i<=high;i++){
		int torf = 0;
		for(int j=2;j*j<=i;j++){
			if(i%j==0){
				torf = 1;
				break;
			}
		}
		if(torf==0){
			printf("%d\n",i);
		}
	}
	return 0;
}