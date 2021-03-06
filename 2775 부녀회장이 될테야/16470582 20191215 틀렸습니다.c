#include <stdio.h>
int main(){
	int n;
	scanf("%d",&n);
	int layer, room;
	int apart[15][14];
	for(int i=0;i<14;i++){
		apart[0][i] = i;
	}
	for(int i=1;i<15;i++){
		for(int j=0;j<14;j++){
			apart[i][j] = 0;
		}
	}
	for(int i=1;i<15;i++){
		for(int j=0;j<14;j++){
			for(int k=0;k<j+1;k++){
				apart[i][j] += apart[i-1][k];
			}
		}
	}
	for(int i=0;i<n;i++){
		scanf("%d",&layer);
		scanf("%d",&room);
		printf("%d\n",apart[layer][room]);
	}
	return 0;
}
