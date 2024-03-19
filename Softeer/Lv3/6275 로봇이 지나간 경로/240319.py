import sys


def delta(x, y):
    count = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if 0 <= a < H and 0 <= b < W and visit[a][b] == '#':
            count += 1
    return count


def find_start():  # 시작점 찾기
    for i in range(H):  # 시작점이 명확하다면
        for j in range(W):
            if visit[i][j] == '#':
                if delta(i, j) == 1:
                    return i, j
    for i in range(H):  # 사이클이 만들어졌다면
        for j in range(W):
            if visit[i][j] == '#':
                return i, j


def initial_d(i, j):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    direction = ['up', 'down', 'left', 'right']
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if 0 <= a < H and 0 <= b < W and visit[a][b] == '#':
            return direction[i]


def move(x, y, d):
    if d == 'up':
        return x - 1, y
    if d == 'down':
        return x + 1, y
    if d == 'left':
        return x, y - 1
    if d == 'right':
        return x, y + 1


def turn(x, y, d, rotate):
    temp1 = {'up': 0, 'right': 1, 'down': 2, 'left': 3}
    temp2 = {0: 'up', 1: 'right', 2: 'down', 3: 'left'}
    if rotate == 'R':
        return temp2[(temp1[d]+1) % 4]
    return temp2[(temp1[d]+3) % 4]
    

input = sys.stdin.readline
H, W = map(int, input().split())
visit = [list(input().strip()) for _ in range(H)]
x, y = find_start()
d = initial_d(x, y)
print(x+1, y+1)
if d == 'up':
    print('^')
elif d == 'down':
    print('v')
if d == 'left':
    print('<')
if d == 'right':
    print('>')

# 움직임 정의하기
command = ''
while True:
    visit[x][y] = '.'
    a, b = move(x, y, d)
    if 0 <= a < H and 0 <= b < W and visit[a][b] == '#':
        command += 'A'
        visit[a][b] = '.'
        x, y = move(a, b, d)
        continue
    a, b = move(x, y, turn(x, y, d, 'R'))
    if 0 <= a < H and 0 <= b < W and visit[a][b] == '#':
        command += 'RA'
        visit[a][b] = '.'
        d = turn(x, y, d, 'R')
        x, y = move(a, b, d)
        continue
    a, b = move(x, y, turn(x, y, d, 'L'))
    if 0 <= a < H and 0 <= b < W and visit[a][b] == '#':
        command += 'LA'
        visit[a][b] = '.'
        d = turn(x, y, d, 'L')
        x, y = move(a, b, d)
        continue
    break
print(command)