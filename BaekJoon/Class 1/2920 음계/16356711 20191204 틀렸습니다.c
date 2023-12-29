#include <stdio.h>

int main() {
	int melody[8];
	for(int i=0;i<8;i++){
		scanf("%d",&melody[i]);
	}
	int as=0,de=0;
	for(int i=0;i<8;i++){
		if(melody[i]==i+1){
			as++;
			if(as==8){
				printf("ascending");
				return 0;
			}
		}
		else if(melody[i]+i==8){
			de++;
			if(de==8){
				printf("descending");
				return 0;
			}
		}
		else{
			printf("mixed");
			return 0;
		}
	}
}
