#include <stdio.h>
void Hanoi(int block, int from, int temp, int to);
int main(){
	int n;
	scanf("%d",&n);
	int movingcount = 1;
	for(int i=0;i<n;i++){
		movingcount *= 2;
	}
	printf("%d\n",movingcount-1);
	Hanoi(n,1,2,3);
	return 0;
}
void Hanoi(int block, int from, int temp, int to){
	if(block==1){
		printf("%d %d\n",from,to);
	}
	else{
		Hanoi(block-1,from, to, temp);
		printf("%d %d\n",from, to);//맨 밑 원판을 옮겨주는 작업
		Hanoi(block-1,temp, from, to);
	}
}
/*
1,맨 밑 원판을 제외한 판들을 현재 탑과 목표 탑이 아닌 중간에 쌓는다
2,맨 밑 원판을 목표 탑에 쌓는다->결국 처음에 목표 탑에 제일 큰 원판이 쌓이니까 중간에 어떤 탑에 쌓을지 고민 안해도 되는거같은데
3,현재 중간 탑에 쌓여있는 탑들을 1,2과정 반복해준다
그럼 1을 함수로 표현해줘야할 듯 싶은데 1도 결국 1,2함수의 반복이다
이걸 오래 고민했던 이유는 중간에 만들어지는 탑을 옮겨주는 과정을 생략했기 때문
*/