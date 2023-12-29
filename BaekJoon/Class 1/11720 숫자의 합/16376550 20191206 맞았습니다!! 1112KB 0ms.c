#include <stdio.h>
int main(){
	int n;
	int total = 0;
	scanf("%d",&n);
	char nums[100];
	scanf("%s",nums);
	for(int i=0;i<n;i++){
		total+=nums[i]-48;
	}
	printf("%d",total);
	return 0;
}

