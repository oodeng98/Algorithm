#include <stdio.h>
int main(){
	int n;
	scanf("%d",&n);
	for(int i=1;i<10000;i++){
		if(n>i){
			n-=i;
		}
		else{
			if((i+1)%2==0){
				printf("%d/%d",i+1-n,n);
				return 0;
			}
			else{
				printf("%d/%d",n,i+1-n);
				return 0;
			}
		}
	}
}
