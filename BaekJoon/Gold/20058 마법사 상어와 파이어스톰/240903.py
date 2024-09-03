import sys


input = sys.stdin.readline

def delta(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if 0 <= a < 2 ** N and 0 <= b < 2 ** N:
            grid_check[a][b] += 1
    return


def turn_right(i, j, side_length):
    for a in range(side_length):
        for b in range(side_length):
            new_grid[i + b][j - a + side_length - 1] = grid[i + a][j + b]
            if 0 < new_grid[i + b][j + side_length - a - 1]:
                delta(i + b, j + side_length - a - 1)
    

N, Q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(2 ** N)]
for L in map(int, input().split()):
    new_grid = [[0 for _ in range(2 ** N)] for _ in range(2 ** N)]
    grid_check = [[0 for _ in range(2 ** N)] for _ in range(2 ** N)]
    for i in range(2 ** (N - L)):
        for j in range(2 ** (N - L)):
            turn_right(2 ** L * i, 2 ** L * j, 2 ** L)
    for i in range(2 ** N):
        for j in range(2 ** N):
            if grid_check[i][j] < 3:
                new_grid[i][j] -= 1
    grid = new_grid
    

result1 = 0
for i in grid:
    for j in i:
        result1 += max(j, 0)
print(result1)

check = [[0 for _ in range(2 ** N)] for _ in range(2 ** N)]
count = 0
for i in range(2 ** N):
    for j in range(2 ** N):
        if 0 < grid[i][j]:
            stack = [(i, j)]
            temp = 0
            while stack:
                x, y = stack.pop()
                if check[x][y]:
                    continue
                check[x][y] = 1
                temp += 1
                dx = [-1, 1, 0, 0]
                dy = [-0, 0, -1, 1]
                for i in range(4):
                    a = x + dx[i]
                    b = y + dy[i]
                    if 0 <= a < 2 ** N and 0 <= b < 2 ** N:
                        if 0 < grid[a][b]:
                            stack.append((a, b))
            count = max(count, temp)
print(count)