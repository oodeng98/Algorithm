#include <stdio.h>
int main(){
	int low,high;
	scanf("%d",&low);
	scanf("%d",&high);
	int total = 0;
	int num[10000];
	int lownum=0;
	for(int i=low;i<=high;i++){
		int torf = 0;
		for(int j=2;j<=i/2;j++){
			if(i%j==0){
				torf = 1;
				break;
			}
		}
		if(torf==0){
			total+=i;
			num[lownum] = i;
			lownum++;
		}
	}
	if(total==0){
		printf("-1");
		return 0;
	}
	printf("%d\n%d",total,num[0]);
	return 0;
}