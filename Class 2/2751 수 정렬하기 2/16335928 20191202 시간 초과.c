#include <stdio.h>

int main() {
	int number;
	scanf("%d",&number);
	int numbers[1000000];
	for(int i=0;i<number;i++){
		scanf("%d",&numbers[i]);
	}
	int temp;
	for(int i=1;i<number;i++){
		if(numbers[i-1]>numbers[i]){
			temp = numbers[i-1];
			numbers[i-1] = numbers[i];
			numbers[i] = temp;
			i = 0;
			continue;
		}
	}
	for(int i=0;i<number;i++){
		printf("%d\n",numbers[i]);
	}
	return 0;
}