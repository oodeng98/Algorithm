#include <stdio.h>

int main(){
	char white[8][8];
	char black[8][8];
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			white[2*i][2*j+1] = 'W';
			white[2*i+1][2*j] = 'B';
			black[2*i][2*j+1] = 'B';
			black[2*i+1][2*j] = 'W';
		}
	}
	int length, height;
	scanf("%d",&height);
	scanf("%d",&length);
	char board[height][length+1];
	for(int i=0;i<height;i++){
		scanf("%s",board[i]);
	}
	int count = height*length;
	int whiteprecount = 0;
	int blackprecount = 0;
	for(int i=0;i<height-7;i++){
		for(int j=0;j<length-7;j++){
			for(int k=0;k<8;k++){
				for(int l=0;l<8;l++){
					if(board[i+k][j+l]!=white[k][l]){
						whiteprecount++;
					}
					if(board[i+k][j+l]!=black[k][l]){
						blackprecount++;
					}
				}
			}
			if(count>whiteprecount){
				count = whiteprecount;
			}
			if(count>blackprecount){
				count = blackprecount;
			}
			whiteprecount = 0;
			blackprecount = 0;
		}
	}
	printf("\n%d",count);
	return 0;
}