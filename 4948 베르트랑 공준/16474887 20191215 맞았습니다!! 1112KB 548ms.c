#include <stdio.h>
int main(){
	int t=1;
	while(1){
		scanf("%d",&t);
		if(t==0){
			break;
		}
		int count = 0;
		for(int i=t+1;i<=2*t;i++){
			int torf = 0;
			for(int j=2;j*j<=i;j++){
				if(i%j==0){
					torf = 1;
					break;
				}
			}
			if(torf==0){
				count++;
			}
		}
		printf("%d\n",count);
	}
	return 0;
}