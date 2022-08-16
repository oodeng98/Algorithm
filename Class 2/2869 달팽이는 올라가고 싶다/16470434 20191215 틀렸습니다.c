#include <stdio.h>
int main(){
	int height,up,down;
	scanf("%d",&up);
	scanf("%d",&down);
	scanf("%d",&height);
	int day = ((height-up)/(up-down))+1;
	printf("%d",day);
}
