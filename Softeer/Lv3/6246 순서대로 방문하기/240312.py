def delta(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        a, b = x + dx[i], y + dy[i]
        if 0 <= a < N and 0 <= b < N and arr[a][b] == 0:
            yield a, b
            

def dfs(x, y, n):        
    if n == M:
        visited[x][y] += 1
    if visited[x][y] != 0:
        return
    visited[x][y] = 1
    for a, b in delta(x, y):
        if (a, b) in target:
            if target[(a, b)] == n + 1:
                dfs(a, b, n+1)
        else:
            dfs(a, b, n)
    visited[x][y] = 0
    


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
target = {}
for i in range(1, M+1):
    a, b = map(int, input().split())
    temp = (a - 1, b - 1)
    target[temp] = i
    if i == 1:
        start = temp
    elif i == N:
        finish = temp
visited = [[0 for _ in range(N)] for _ in range(N)]
# print(target)
dfs(*start, 1)
print(visited[a-1][b-1])