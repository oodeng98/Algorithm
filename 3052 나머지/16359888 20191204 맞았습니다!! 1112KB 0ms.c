#include <stdio.h>

int main(){
	int num[10];
	int last[10];
	int count = 10;
	for(int i=0;i<10;i++){
		scanf("%d",&num[i]);
		last[i] = num[i]%42;
	}
	for(int i=1;i<10;i++){
		for(int j=0;j<i;j++){
			if(last[i]==last[j]){
				count--;
				last[i] = 42+i;
			}
		}
	}
	printf("%d",count);
	return 0;
}
