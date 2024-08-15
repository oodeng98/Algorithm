import sys

input = sys.stdin.readline


def flutter(r, c, direction):
    sand = grid[r][c]
    ret = 0
    if direction == 0:  # 좌
        dic = {(r-2, c): 2, (r-1, c-1): 10, (r-1, c): 7, (r-1, c+1): 1, (r+2, c): 2, (r+1, c-1): 10, (r+1, c): 7, (r+1, c+1): 1, (r, c-2): 5}
        a, b = r, c-1
    elif direction == 2:  # 우
        dic = {(r-2, c): 2, (r-1, c-1): 1, (r-1, c): 7, (r-1, c+1): 10, (r+2, c): 2, (r+1, c-1): 1, (r+1, c): 7, (r+1, c+1): 10, (r, c+2): 5}
        a, b = r, c+1
    elif direction == 1:  # 하
        dic = {(r, c-2): 2, (r-1, c-1): 1, (r, c-1): 7, (r+1, c-1): 10, (r, c+2): 2, (r-1, c+1): 1, (r, c+1): 7, (r+1, c+1): 10, (r+2, c): 5}
        a, b = r+1, c
    else:  # 상
        dic = {(r, c-2): 2, (r-1, c-1): 10, (r, c-1): 7, (r+1, c-1): 1, (r, c+2): 2, (r-1, c+1): 10, (r, c+1): 7, (r+1, c+1): 1, (r-2, c): 5}
        a, b = r-1, c
    for i, j in dic:
        fly = sand * dic[(i, j)] // 100
        grid[r][c] -= fly
        if 0 <= i < N and 0 <= j < N:
            grid[i][j] += fly
        else:
            ret += fly
            
    if 0 <= a < N and 0 <= b < N:
        grid[a][b] += grid[r][c]
    else:
        ret += grid[r][c]
    grid[r][c] = 0
    return ret

def move():
    r, c = N // 2, N // 2
    ret = 0
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    # 좌, 하, 우, 상 순서
    
    direction = 0
    count = 1
    while True:
        dr = dx[direction % 4]
        dc = dy[direction % 4]
        for _ in range(direction // 2 + 1):
            r += dr
            c += dc
            ret += flutter(r, c, direction % 4)
            count += 1
            if count == N ** 2:
                return ret
        direction += 1

        
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
print(move())
