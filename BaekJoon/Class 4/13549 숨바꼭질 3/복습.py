def BOJ13549():
    def c(start, des):
        if start >= des:  # 목적지를 지나쳤다면
            return start - des
        elif des == 1:  # 목적지가 1이고 출발지가 0이라면
            return 1
        elif des % 2:  # 목적지가 홀수라면
            return 1 + min(c(start, des - 1), c(start, des + 1))  # 목적지를 짝수로 바꿔주는 역할
        else:  # 목적지가 짝수라면
            return min(des - start, c(start, des // 2))
    n, k = map(int,input().split())
    print(c(n, k))
BOJ13549()