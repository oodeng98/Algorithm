#include <stdio.h>

int main() {
	int a,b;
	scanf("%d",&a);
	int high ,low;
	scanf("%d",&high);
	scanf("%d",&low);
	if(a<3){
		if(high<low){
			int temp = low;
			low = high;
			high = temp;
		}
	}
	else{
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
