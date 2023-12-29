#include <stdio.h>
int main(){
	int radius;
	scanf("%d",&radius);
	float euclid,taxi;
	euclid = radius*radius*3.14159265;
	taxi = 2*radius*radius;
	printf("%lf\n%lf",euclid,taxi);
	return 0;
}