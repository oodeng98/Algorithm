#include <stdio.h>
int main(){
	char word[100];
	int alphabet[26];
	for(int i=0;i<26;i++){
		alphabet[i] = -1;
	}
	scanf("%s",word);
	int end;
	for(int i=0;i<100;i++){
		if(word[i]==NULL){
			end = i+1;
			break;
		}
	}
	for(int i=0;i<end-1;i++){
		for(int j=0;j<26;j++){
			if(word[i]=='a'+j){
				if(alphabet[j]==-1){
					alphabet[j] = i;
				}
				break;
			}
		}
	}
	for(int i=0;i<26;i++){
		printf("%d ",alphabet[i]);
	}
	return 0;
}

