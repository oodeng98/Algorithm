#include <stdio.h>

int n, cnt=1, isok, temp,i;
int main() {
	scanf("%d", &n);
	if(n==1){
		printf("666");
		return 0;
	}
	for(i=667;;i++){
		temp = i;
		isok = 0;
		while (temp) {
			if (temp % 1000 == 666) {
				isok = 1;
				break;
			}
			temp /= 10;
		}
		if (isok) {
			cnt++;
			if (cnt == n)
				break;
		}
	}
	printf("%d", i);
	return 0;
}