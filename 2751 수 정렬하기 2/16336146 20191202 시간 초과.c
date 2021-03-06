#include <stdio.h>

int main() {
	int number;
	scanf("%d",&number);
	int numbers[1000000];
	numbers[0] = 0;
	for(int i=0;i<number;i++){
		scanf("%d",&numbers[i]);
		for(int j=0;j<i;j++){
			if(numbers[i]>numbers[j]){
				continue;
			}
			else if(numbers[i]<numbers[j]){
				int temp = numbers[j];
				numbers[j] = numbers[i];
				for(int k=i;k>j;k--){
					numbers[k] = numbers[k-1];
				}
				numbers[j+1] = temp;
			}
		}
	}
	for(int i=0;i<number;i++){
		printf("%d\n",numbers[i]);
	}
	return 0;
}