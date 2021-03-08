import sys


input = sys.stdin.readline
num = int(input())

for i in range(num):
    m, n, x, y = map(int, input().split())
    if m > n:  # n을 더 큰 값으로 둔다
        m, n = n, m
        x, y = y, x
    # if (x - y) % 2 == 1 and m % 2 == 0:
    #     print(-1)
    # elif m == n and x != y:
    #     print(-1) 
    # 예외처리 구간 제거
    result = y - x
    j = 0
    while result % m != 0:
        result += n
        j += 1
        if j > m:
            break
    if j > m:
        print(-1)
        continue
    print(result + x)