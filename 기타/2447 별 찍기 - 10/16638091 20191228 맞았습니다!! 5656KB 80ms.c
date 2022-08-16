#include <stdio.h>
int square(int input,int originalinput, char *arraypoint, int repeat);
int main(){
	int n;
	scanf("%d",&n);
	char star[n][n];
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			star[i][j] = '*';
		}
	}
	char *starpoint = star;
	square(n,n,starpoint,1);//이거 수정해줘야함
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			printf("%c",star[i][j]);
		}
		printf("\n");
	}
	return 0;
}
int square(int input, int originalinput, char *arraypoint, int repeat){
	if(input==1){
		return 1;
	}
	for(int x=0;x<repeat;x++){
		for(int y=0;y<repeat;y++){
			for(int i=input/3+input*x;i<input/3*2+input*x;i++){
				for(int j=input/3+input*y;j<input/3*2+input*y;j++){
					*(arraypoint+originalinput*i+j) = ' ';
				}
			}
		}
	}
	return square(input/3, originalinput, arraypoint,repeat*3);
}