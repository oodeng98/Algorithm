#include <stdio.h>
int main(){
	int n;
	scanf("%d",&n);
	int count=0;
	for(int i=0;i<n;i++){
		int TorF,OnlyoneWord;
		char word[101];
		scanf("%s",word);
		int alphabet[26];//word에 들어있는 알파벳의 종류 및 개수를 보관하는 곳
		for(int j=0;j<26;j++){
			alphabet[j]=0;
		}
		for(int j=0;j<26;j++){
			alphabet[j]=0;
		}
		for(int j=0;word[j]!=NULL;j++){//같은 알파벳을 찾아서 인덱스값을 배열에 저장한 후 크기별로 정리해준 후 값이 1이상 차이나는게 있나 확인하면 될듯
			alphabet[word[j]-'a']++;
		}
		for(int j=0;j<26;j++){
			if(alphabet[j]>1){
				int temp = -1;
				for(int k=0;word[k]!=NULL;k++){
					if(word[k]=='a'+j){
						if(temp==-1){
							temp = k;
						}
						else{
							if(k-temp!=1){
								TorF = -1;
								break;
							}
						}
					}
				}
			}
			else{
				OnlyoneWord++;
				if(OnlyoneWord==26){
					count++;
				}
			}
		}
		if(TorF!=-1){
			count++;
		}
	}
	printf("%d",count);
	return 0;
}

