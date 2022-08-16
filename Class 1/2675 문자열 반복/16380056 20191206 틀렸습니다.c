#include <stdio.h>
int main(){
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		int num;
		scanf("%d",&num);
		char word[21];
		scanf("%s",word);
		int j=0;
		while(word[j]!=NULL){
			for(int i=0;i<num;i++){
				printf("%c",word[j]);
			}
			j++;
		}
	}
	printf("\n");
	return 0;
}
