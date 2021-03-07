#include <stdio.h>
int main(){
	int pointX,pointY,rightX,rightY;
	scanf("%d",&pointX);scanf("%d",&pointY);scanf("%d",&rightX);scanf("%d",&rightY);
	//그냥 x,y와 꼭짓점과 x,y의 차이 이 네가지를 다 비교해줘야함
	int smallestValue = pointX;
	for(int i=0;i<4;i++){
		if(smallestValue>pointY){
			smallestValue = pointY;
		}
		else if(smallestValue>rightX-pointX){
			smallestValue = rightX-pointX;
		}
		else if(smallestValue>rightY-pointY){
			smallestValue = rightY-pointY;
		}
	}
	printf("%d",smallestValue);
	return 0;
}