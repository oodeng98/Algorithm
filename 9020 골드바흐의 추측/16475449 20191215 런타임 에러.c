#include <stdio.h>
int main(){
	typedef struct{
		int first;
		int second;
	}twin;
	int t;
	scanf("%d",&t);
	int sosu[2000];
	int index = 0;
	twin twins[100];
	for(int i=2;i<=10000;i++){
		int torf = 0;
		for(int j=2;j*j<=i;j++){
			if(i%j==0){
				torf = 1;
				break;
			}
		}
		if(torf==0){
			sosu[index] = i;
			index++;
		}
	}
	for(int i=0;i<t;i++){
		int indexs=0;
		int n;
		scanf("%d",&n);
		for(int j=0;sosu[j]<n;j++){
			for(int k=0;sosu[k]<n;k++){
				if(sosu[j]+sosu[k]==n){
					twins[indexs].first = sosu[j];
					twins[indexs].second = sosu[k];
					indexs++;
				}
			}
		}
		int low = twins[0].second - twins[0].first;;
		int twinindex = 0;
		for(int j=1;j<indexs;j++){
			if(twins[j].second<twins[j].first){
				int temp = twins[j].first;
				twins[j].first = twins[j].second;
				twins[j].second = temp;
			}
			int temp = twins[j].second - twins[j].first;
			if(temp<low){
				low = temp;
				twinindex = j;
			}
		}
		printf("%d %d\n",twins[twinindex].first,twins[twinindex].second);
	}
	return 0;
}
