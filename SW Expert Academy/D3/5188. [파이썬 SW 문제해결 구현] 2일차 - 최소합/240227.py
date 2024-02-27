import sys

sys.stdin = open('input.txt')


def delta(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        if 0 <= x + dx[i] < N and 0 <= y + dy[i] < N:
            yield x + dx[i], y + dy[i]


def dfs(x, y):
    for a, b in delta(x, y):
        if visited[x][y] + arr[a][b] < visited[a][b]:
            visited[a][b] = visited[x][y] + arr[a][b]
            dfs(a, b)



T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[float('inf') for _ in range(N)] for _ in range(N)]
    visited[0][0] = arr[0][0]
    dfs(0, 0)
    print(f"#{t} {visited[N-1][N-1]}")