#include <stdio.h>
int main(){
	char word[102];
	scanf("%s",word);
	int end;
	for(int i=0;i<101;i++){
		if(word[i]==NULL){
			end = i;
			break;
		}
	}
	for(int i=0;i<end;i++){
		if(word[i]=='c'){
			if(word[i+1]=='='){
				end--;
			}
			else if(word[i+1]=='-'){
				end--;
			}
		}
		else if(word[i]=='d'){
			if(word[i+1]=='z'){
				if(word[i+2]=='='){
					end--;
					end--;
				}
			}
			else if(word[i+1]=='-'){
				end--;
			}
		}
		else if(word[i]=='l'){
			if(word[i+1]=='j'){
				end--;
			}
		}
		else if(word[i]=='n'){
			if(word[i+1]=='j'){
				end--;
			}
		}
		else if(word[i]=='s'){
			if(word[i+1]=='='){
				end--;
			}
		}
		else if(word[i]=='z'){
			if(word[i+1]=='='){
				end--;
			}
		}
	}
	printf("%d",end);
	return 0;
}
