#include <stdio.h>
int main(){
	typedef struct{
		int first;
		int second;
	}twin;
	int t;
	scanf("%d",&t);//횟수 입력
	int sosu[2000];//소수 모음집
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
	}//소수 모음집에 소수 넣는 과정
	for(int i=0;i<t;i++){
		int indexs=0;
		int n;
		scanf("%d",&n);
		for(int j=0;sosu[j]<n;j++){//입력받은 짝수보다 작은 값의 소수들만 확인
			for(int k=0;sosu[k]-sosu[j]<n;k++){//마찬가지
				if(sosu[j]+sosu[k]==n){
					twins[indexs].first = sosu[j];
					twins[indexs].second = sosu[k];
					indexs++;//경우의 수가 여러개가 나올 수 있어서 그 경우의 수의 인덱스값을 저장해놓는 변수
				}
			}
		}
		int low = twins[0].second - twins[0].first;
		if(low<0){
			low = twins[0].first - twins[0].second;
		}
		int twinindex = 0;
		for(int j=0;j<indexs;j++){
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