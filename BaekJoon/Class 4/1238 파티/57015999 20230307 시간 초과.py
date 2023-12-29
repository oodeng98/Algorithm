import sys


input = sys.stdin.readline
n, m, x = map(int, input().split())
dist = [[float('inf') for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a - 1][b - 1] = c
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
ret = 0
for i in range(n):
    ret = max(dist[i][x] + dist[x][i], ret)
print(ret)