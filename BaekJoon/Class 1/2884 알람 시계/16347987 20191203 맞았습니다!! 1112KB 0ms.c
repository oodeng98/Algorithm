#include <stdio.h>

int main() {
	int h;//hour
	int m;//minute
	scanf("%d",&h);
	scanf("%d",&m);
	if(m<=45){
		m+=15;
		h-=1;
		if(m==60){
			h+=1;
			m=0;
		}
		else if(h<0){
			h+=24;
		}
		else if(h==24){
			h = 0;
		}
	}
	else{
		m-=45;
	}
	printf("%d %d",h,m);
	return 0;
}
