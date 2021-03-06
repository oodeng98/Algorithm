#include <stdio.h>
int main(){
	int n;
	int height, low, order;
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		scanf("%d",&height);
		scanf("%d",&low);
		scanf("%d",&order);
		int tf=1;
		while(order>height){
			order-=height;
			tf++;
		}
		if(tf<10){
			printf("%d0%d\n",order,tf);
		}
		else{
			printf("%d%d\n",order,tf);
		}
	}
}
