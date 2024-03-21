import sys
from collections import deque


def delta(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if 0 <= a < N and 0 <= b < N:
            yield a, b


def bfs():
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        for a, b in delta(x, y):
            cost = visit[x][y] + 1 + max(arr[a][b] - arr[x][y], 0)
            if visit[a][b] <= cost:
                continue
            visit[a][b] = cost
            queue.append((a, b))


sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[float('inf') for _ in range(N)] for _ in range(N)]
    visit[0][0] = 0
    bfs()
    print(f"#{t} {visit[N-1][N-1]}")