int main(){
    /*노트북 판매 대수와 상관없이 A만원의 지출
    한대의 노트북을 생산하는 것에 B만원의 지출
    노트북의 가격이 C만원으로 책정된다고 하면 손익분기점을 구하라*/
    int A,B,C;
    scanf("%d",&A);
    scanf("%d",&B);
    scanf("%d",&C);
    int result=0;
    while((A+B*result)<C*result){
        result++;
        if(B>C){
            printf("-1");
        }
    }
    return 0;
}