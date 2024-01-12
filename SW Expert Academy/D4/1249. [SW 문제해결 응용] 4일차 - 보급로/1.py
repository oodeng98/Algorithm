def around(x, y):
    ret = []
    if x + 1 < N:
        ret.append((x + 1, y))
    if y + 1 < N:
        ret.append((x, y + 1))
    if 0 <= y - 1:
            ret.append((x, y - 1))
    if 0 <= x - 1:
        ret.append((x - 1, y))

    return ret


def bfs(x, y):
    if x == N - 1 and y == N - 1:
        return
    candidate = around(x, y)
    for a, b in candidate:
        if Map[a][b] + score[x][y] < score[a][b]:
            score[a][b] = Map[a][b] + score[x][y]
            bfs(a, b)


T = int(input())

for t in range(T):
    N = int(input())
    Map = []
    for _ in range(N):
        Map.append(list(input()))
    for i in range(N):
        for j in range(N):
            Map[i][j] = int(Map[i][j])

    score = [[float('inf') for _ in range(N)] for _ in range(N)]
    score[0][0] = 0
    bfs(0, 0)
    
    print(f"#{t+1} {score[N-1][N-1]}")