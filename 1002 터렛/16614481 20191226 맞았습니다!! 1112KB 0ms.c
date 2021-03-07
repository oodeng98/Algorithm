#include <stdio.h>
int main(){
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		int jx,jy,bx,by,jr,br;
		scanf("%d",&jx);scanf("%d",&jy);scanf("%d",&jr);scanf("%d",&bx);scanf("%d",&by);scanf("%d",&br);
		if(jx==bx&&jy==by){
			if(jr==br){
				printf("-1\n");
				continue;
			}
			else{
				printf("0\n");
				continue;
			}
		}
		else{
			if((jx-bx)*(jx-bx)+(jy-by)*(jy-by)>(jr+br)*(jr+br)){
				printf("0\n");
				continue;
			}
			else if((jx-bx)*(jx-bx)+(jy-by)*(jy-by)==(jr+br)*(jr+br)||(jx-bx)*(jx-bx)+(jy-by)*(jy-by)==(jr-br)*(jr-br)){
				printf("1\n");
				continue;
			}
			else if((jx-bx)*(jx-bx)+(jy-by)*(jy-by)<(jr-br)*(jr-br)){
				printf("0\n");
				continue;
			}
			else{
				printf("2\n");
				continue;
			}
		}
	}
	return 0;
}