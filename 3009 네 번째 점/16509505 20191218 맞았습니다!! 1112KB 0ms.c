#include <stdio.h>
typedef struct{
	int pointX;
	int pointY;
}squarepoint;
int main(){
	squarepoint square[3];
	for(int i=0;i<3;i++){
		scanf("%d",&square[i].pointX);
		scanf("%d",&square[i].pointY);
	}
	int targetpointX,targetpointY;
	for(int i=0;i<3;i++){
		for(int j=0;j<3&&j!=i;j++){
			if(square[i].pointX==square[j].pointX){
				targetpointX = square[3-i-j].pointX;
			}
			if(square[i].pointY==square[j].pointY){
				targetpointY = square[3-i-j].pointY;
			}
		}
	}
	printf("%d %d",targetpointX,targetpointY);
	return 0;
}