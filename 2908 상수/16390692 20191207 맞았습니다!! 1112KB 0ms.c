#include <stdio.h>
int main(){
	int num1,num2;
	scanf("%d",&num1);
	scanf("%d",&num2);
	int num11[3];int num22[3];
	num11[0]=num1%10;
	num11[1]=(num1%100-num1%10)/10;
	num11[2]=num1/100;
	num22[0]=num2%10;
	num22[1]=(num2%100-num2%10)/10;
	num22[2]=num2/100;
	if((num11[0]*100+num11[1]*10+num11[2])>(num22[0]*100+num22[1]*10+num22[2])){
		printf("%d",(num11[0]*100+num11[1]*10+num11[2]));
	}
	else{
		printf("%d",(num22[0]*100+num22[1]*10+num22[2]));
	}
	return 0;
}
