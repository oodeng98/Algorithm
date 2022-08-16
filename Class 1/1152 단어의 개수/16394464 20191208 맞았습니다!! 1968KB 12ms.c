#include <stdio.h>
int main(){
	char word[1000001];
	scanf("%[^\n]",word);
	int count = 1;
	int end,start;
	for(int i=0;i<1000001;i++){
		if(word[i]==NULL){
			end = i-1;
			break;
		}
	}
	for(int i=0;i<1000001;i++){
		if(word[i]!=' '){
			start = i;
			break;
		}
	}
	if(word[0]==' '&&word[1]==NULL){
		printf("0");
		return 0;
	}
	for(int i=start;word[i]!=NULL;i++){
		if(word[i]==' '){
			if(i==0){
				continue;
			}
			else if(i==end){
				break;
			}
			else
				count++;
		}

	}
	printf("%d",count);
	return 0;
}

