#include <stdio.h>
int main(){
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		long long int now,des;
		scanf("%lld",&now);
		scanf("%lld",&des);
		long long int length = des-now;
		if(length == 1){
			printf("1\n");
			continue;
		}
		else if(length == 2){
			printf("2\n");
			continue;
		}
		long long int pn = 1;
		for(int j=2;j<1000000;j++){
			pn+=j;
			if(length<=pn*2){
				if(pn*2-length<j){
					printf("%lld\n",2*j);
				}
				else{
					printf("%lld\n",2*j-1);
				}
				break;
			}
		}
	}
	return 0;
}