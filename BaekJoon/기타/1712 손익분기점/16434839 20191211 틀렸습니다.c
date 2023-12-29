#include <stdio.h>
int main(){
	int a,b,c;
	scanf("%d",&a);
	scanf("%d",&b);
	scanf("%d",&c);
	int i=0;
	while(a+i*b>=i*c){
		if(b>=c){
			printf("-1");
			break;
		}
		else{
			i++;
		}
	}
	printf("%d",i);
	return 0;
}