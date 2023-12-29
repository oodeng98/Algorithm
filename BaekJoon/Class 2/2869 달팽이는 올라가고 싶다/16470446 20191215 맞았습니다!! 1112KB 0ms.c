#include <stdio.h>
int main(){
	int height,up,down;
	scanf("%d",&up);
	scanf("%d",&down);
	scanf("%d",&height);
	int day = ((height-up)/(up-down))+1;
	if((height-up)%(up-down)!=0){
		day++;
	}
	printf("%d",day);
}
