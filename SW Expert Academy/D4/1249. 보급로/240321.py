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
    visit[0][0] = 0
    while queue:
        x, y = queue.popleft()
        for a, b in delta(x, y):
            if visit[a][b] <= visit[x][y] + arr[a][b]:
                continue
            visit[a][b] = visit[x][y] + arr[a][b]
            queue.append((a, b))
    return visit[N-1][N-1]
             
 
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visit = [[float('inf') for _ in range(N)] for _ in range(N)]
    print(f"#{t} {bfs()}")