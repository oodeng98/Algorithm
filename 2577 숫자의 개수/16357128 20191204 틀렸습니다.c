#include <stdio.h>

int main(){
	int one,two,three;
	scanf("%d",&one);
	scanf("%d",&two);
	scanf("%d",&three);
	int total = one*two*three;
	int count[10];
	for(int i=0;i<10;i++){
		count[i]=0;
	}
	int n=100;
	count[total%10]++;
	while(total*10>n){
		count[(total%n-total%(n/10))*10/n]++;
		n*=10;
	}
	for(int i=0;i<10;i++){
		printf("%d\n",count[i]);
	}
	return 0;
}
