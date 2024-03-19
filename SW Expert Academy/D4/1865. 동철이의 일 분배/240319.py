import sys


def distribute(n, prob):
    if n == N:
        result[0] = max(result[0], prob)
        return 
    if prob <= result[0]:
        return
    for i in range(N):
        if visit[i]:
            continue
        visit[i] = 1
        distribute(n+1, prob * arr[n][i])
        visit[i] = 0


sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(N)]
    result = [0]
    visit = [0 for _ in range(N)]
    distribute(0, 1)
    print(f"#{t} {format(result[0] * 100, '.6f')}")