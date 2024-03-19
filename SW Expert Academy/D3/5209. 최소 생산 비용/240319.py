import sys


def cal(n, total):
    if n == N:
        result[0] = min(result[0], total)
        return
    if result[0] <= total:
        return
    for i in range(N):
        if visit[i]:
            continue
        total += arr[n][i]
        visit[i] = 1
        cal(n+1, total)
        total -= arr[n][i]
        visit[i] = 0


sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0 for _ in range(N)]
    result = [float('inf')]
    cal(0, 0)
    print(f"#{t} {result[0]}")