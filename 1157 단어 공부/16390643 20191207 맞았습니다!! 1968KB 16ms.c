#include <stdio.h>
int main(){
	char word[1000001];scanf("%s",word);
	int max=0;int j=0;int alphabet[26];int count=0;int index;
	for(int i=0;i<26;i++){
		alphabet[i]=0;
	}
	while(word[j]!=NULL){
		if(word[j]>='a'&&word[j]<='z'){
			word[j]-='a'-'A';
		}
		alphabet[word[j]-'A']++;
		j++;
	}
	for(int i=0;i<26;i++){
		if(max<alphabet[i]){
			max = alphabet[i];
			index = i;
		}
	}
	for(int i=0;i<26;i++){
		if(alphabet[i]==max){
			count++;
		}
	}
	if(count==1){
		printf("%c",index+'A');
	}
	else{
		printf("?");
	}

	return 0;
}
