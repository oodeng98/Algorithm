#include <stdio.h>

int main() {
	int h;//hour
	int m;//minute
	scanf("%d",&h);
	scanf("%d",&m);
	if(m-45<0){
		m+=15;
		h-=1;
		if(h<0){
			h+=24;
		}
	}
	printf("%d %d",h,m);
	return 0;
}
