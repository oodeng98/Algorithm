import sys


input = sys.stdin.readline
num = int(input())

for i in range(num):
    m, n, x, y = map(int, input().split())
    if m > n:  # n을 더 큰 값으로 둔다면?
        m, n = n, m
        x, y = y, x
    if abs(x - y) % 2 == 1 and n % 2 == 0:
        # 분자가 계속 홀수다 => 분모가 홀수만 가능하다
        # 계속 홀수인 경우-> y-x가 홀수인 경우+n이 짝수인 경우
        print(-1)
    elif m == n and x != y:
        print(-1)
    else:
        result = y - x
        while result % m != 0:
            result += n
        print(result + x)
# result % m == x
# result % n == y

"""
15
40000 39999 39999 39998
40000 39999 40000 39999
40000 40000 40000 39999
40000 39998 40000 39997
39999 2 39998 2
3 40000 3 39999
40000 3 40000 3
8 2 4 2
10 12 2 12
12 10 12 10
12 10 1 1
12 6 12 6
10 1 5 1
1 10 1 5
1 1 1 1

1599959999
1599960000
-1
-1
39998
39999
120000
4
12
60
1
12
5
5
1
"""