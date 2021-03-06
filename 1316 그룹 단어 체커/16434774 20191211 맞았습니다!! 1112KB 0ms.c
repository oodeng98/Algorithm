#include <stdio.h>
int main(){
	int n;
	scanf("%d",&n);
	int count=0;
	for(int i=0;i<n;i++){
		int TorF=0,OnlyoneWord=0;
		char word[101];
		scanf("%s",word);
		int alphabet[26];
		for(int j=0;j<26;j++){
			alphabet[j]=0;
		}
		for(int j=0;word[j]!=NULL;j++){
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
							if(k-temp==1){
								temp = k;
							}
							else{
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
					TorF = 1;
				}
			}
		}
		if(TorF==0||TorF==1){
			count++;
		}
	}
	printf("%d",count);
	return 0;
}

