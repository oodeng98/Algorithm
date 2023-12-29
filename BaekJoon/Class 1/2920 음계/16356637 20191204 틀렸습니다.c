#include <stdio.h>

int main() {
	int melody[8];
	for(int i=0;i<8;i++){
		scanf("%d",&melody[i]);
	}
	for(int i=0;i<8;i++){
		if(melody[i]==i+1){
			if(i==7){
				printf("ascending");
				return 0;
			}
			continue;
		}
		else if(melody[i]+i==8){
			if(i==7){
				printf("descending");
				return 0;
			}
			continue;
		}
		else{
			printf("mixed");
			return 0;
		}
	}
}
