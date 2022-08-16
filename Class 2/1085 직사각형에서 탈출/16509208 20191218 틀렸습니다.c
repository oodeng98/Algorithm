#include <stdio.h>
int main(){
	int pointX,pointY;
	int rightX,rightY;
	scanf("%d",&pointX);
	scanf("%d",&pointY);
	scanf("%d",&rightX);
	scanf("%d",&rightY);
	if(rightX-pointX<rightY-pointY){
		printf("%d",rightX-pointX);
	}
	else{
		printf("%d",rightY-pointY);
	}
	return 0;
}