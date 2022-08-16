#include <stdio.h>
int main(){
	char word[1000001];scanf("%s",word);
	int max=0;int j=0;int alphabet[26];
	for(int i=0;i<26;i++){
		alphabet[i]=0;
	}
	while(word[j]!=NULL){
		if(word[j]>='a'&&word[j]<='z'){
			word[j]-='a'-'A';//소문자를 대문자로 바꾸는 과정
		}
		alphabet[word[j]-'A']++;
		j++;
	}
	for(int i=0;i<26;i++){
		if(max<alphabet[i]){
			max = alphabet[i];
		}
	}
	for(int i=0;i<26;i++){
		if(alphabet[i]==max){
			printf("?");
			return 0;
		}
	}
	printf("%c",max+'A');
	return 0;
}
