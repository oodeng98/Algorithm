import sys

sys.stdin = open('input.txt')


def delta(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if 0 <= a < N and 0 <= b < N:
            yield a, b


def dfs(x, y, k, count):
    check = 0
    if visited[x][y]:
        return
    visited[x][y] = 1
    for a, b in delta(x, y):
        if arr[a][b] < arr[x][y]:
            check = 1
            dfs(a, b, k, count+1)
        elif arr[a][b] - k < arr[x][y]:
            check = 1
            temp = arr[a][b]
            arr[a][b] = arr[x][y] - 1
            dfs(a, b, 0, count+1)
            arr[a][b] = temp
    if not check:  # 더이상 갈 곳이 없으면?
        global max_length
        max_length = max(max_length, count)
    visited[x][y] = 0


T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_length = 1
    max_value = 0
    for i in arr:
        for j in i:
            max_value = max(max_value, j)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_value:
                visited = [[0 for _ in range(N)] for _ in range(N)]
                dfs(i, j, K, 1)
    print(f"#{t} {max_length}")