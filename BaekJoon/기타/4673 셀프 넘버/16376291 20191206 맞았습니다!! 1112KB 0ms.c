#include <stdio.h>
int findself(int a){
	int num=a-1;
	while(num>0){//num은 10000이하의 자연수
		if((num+(num/1000)+(num%1000)/100+(num%100)/10+(num%10))==a){
			return 0;
			break;
		}
		num--;
	}
	return a;
	}
int main(){
	for(int i=1;i<10001;i++){
		if(findself(i)==i){
			printf("%d\n",i);
		}
	}
	return 0;
}
