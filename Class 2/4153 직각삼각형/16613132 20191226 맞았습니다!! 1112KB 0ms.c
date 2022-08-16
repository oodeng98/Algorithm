#include <stdio.h>
int findbiggest(int a, int b, int c){
	if(a>=b&&a>=c){
		return a;
	}
	else if(b>=c&&b>=a){
		return b;
	}
	else{
		return c;
	}
}
int main(){
	int a,b,c;
	while(1){
		scanf("%d",&a);
		scanf("%d",&b);
		scanf("%d",&c);
		if(a==0&&b==0&&c==0){
			break;
		}
		int big = findbiggest(a,b,c);
		if(big*big*2==a*a+b*b+c*c){
			printf("right\n");
		}
		else{
			printf("wrong\n");
		}

	}
	return 0;
}