import sys

sys.stdin = open('input.txt')


def find_start():
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return i, j
            

def delta(x, y):
    for a, b in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= x + a < N and 0 <= y + b < N and maze[x+a][y+b] in ['0', '3']:
            yield x + a, y + b
    return


def dfs():
    start = find_start()
    queue = [start]
    visit = [[0 for _ in range(N)] for _ in range(N)]
    visit[start[0]][start[1]] = 0
    while queue:
        new_queue = []
        for node in queue:
            for x, y in delta(*node):
                if maze[x][y] == '3':
                    return 1
                if visit[x][y] == 0:
                    new_queue.append((x, y))
                    visit[x][y] = 1
        queue = new_queue
    return 0


for t in range(1, 11):
    T = int(input())
    N = 16
    maze = [input().strip() for _ in range(N)]
    print(f"#{t} {dfs()}")