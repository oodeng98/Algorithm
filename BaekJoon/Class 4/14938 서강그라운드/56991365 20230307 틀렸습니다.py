import sys

input = sys.stdin.readline
n, m, r = map(int, input().split())
dist = [[float('inf') for _ in range(n)] for _ in range(n)]
items = list(map(int, input().split()))
for _ in range(r):
    a, b, c = map(int, input().split())
    dist[a - 1][b - 1] = min(dist[a - 1][b - 1], c)
for i in range(n):
    for j in range(n):
        for k in range(n):
            if dist[j][k] > dist[j][i] + dist[i][k]:
                dist[j][k] = dist[j][i] + dist[i][k]
ret = 0
for i in dist:
    temp = 0
    for index, j in enumerate(i):
        if j <= m:
            ret += items[index]
    ret = max(ret, temp)
print(ret)
