#include <stdio.h>
int main(){
	int t;
	scanf("%d",&t);
	int count = t;
	int word[100];
	for(int i=0;i<t;i++){
		scanf("%d",&word[i]);
	}
	for(int i=0;i<t;i++){
		if(word[i]==1){
			count--;
			continue;
		}
		for(int j=2;j<=word[i]/2;j++){
			if(word[i]%j==0){
				count--;
				break;
			}
		}
	}
	printf("%d",count);
	return 0;
}