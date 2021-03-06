#include <stdio.h>
int main(){
	char word[1000001];
	scanf("%[^\n]",word);
	int count = 1;
	int end;
	for(int i=0;;i++){
		if(word[i]==NULL&&word[i+1]==NULL){
			end = i-1;
			break;
		}
	}
	for(int i=0;word[i]!=NULL;i++){
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

