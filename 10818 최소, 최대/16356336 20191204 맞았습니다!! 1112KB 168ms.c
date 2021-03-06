#include <stdio.h>

int main() {
	int a,b;
	scanf("%d",&a);
	int high ,low;
	if(a==2){
		scanf("%d",&high);
		scanf("%d",&low);
		if(high<low){
			int temp = low;
			low = high;
			high = temp;
		}
	}
	else if(a==1){
		scanf("%d",&b);
		printf("%d %d",b,b);
		return 0;
	}
	else{
		scanf("%d",&high);
		scanf("%d",&low);
		if(high<low){
			int temp = low;
			low = high;
			high = temp;
		}
		for(int i=0;i<a-2;i++){
			scanf("%d",&b);
			if(high<b){
				high = b;
			}
			else if(low>b){
				low = b;
			}
		}
	}

	printf("%d %d",low,high);
	return 0;
}
