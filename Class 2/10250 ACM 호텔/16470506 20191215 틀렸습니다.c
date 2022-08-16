#include <stdio.h>
int main(){
	//무조건 1호 먼저 주고 그다음 2호를 주지만 낮은 층수부터 준다 이건가
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
			printf("%d0%d",order,tf);
		}
		else{
			printf("%d%d",order,tf);
		}
	}
}
