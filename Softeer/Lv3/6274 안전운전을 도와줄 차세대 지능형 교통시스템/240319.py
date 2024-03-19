import sys


def dfs(x, y, time, direction):
    if T < time:
        return
    if 0 <= x < N and 0 <= y < N:
        s = signal[x][y][time % 4]
        visit.add((x, y))
        if direction in s:
            temp = s[direction]
            del s[direction]
            for d in temp:
                dfs(*move(x, y, d), time+1, d)


def move(x, y, direction):
    if direction == 'up':
        return x - 1, y
    if direction == 'down':
        return x + 1, y
    if direction == 'left':
        return x, y - 1
    if direction == 'right':
        return x, y + 1


input = sys.stdin.readline
signal_lst = [
    0, 
    {'right': ['up', 'right', 'down']}, 
    {'up': ['left', 'up', 'right']}, 
    {'left': ['up', 'left', 'down']}, 
    {'down': ['left', 'down', 'right']}, 
    {'right': ['up', 'right']}, 
    {'up': ['left', 'up']}, 
    {'left': ['left', 'down']}, 
    {'down': ['down', 'right']}, 
    {'right': ['right', 'down']}, 
    {'up': ['up', 'right']}, 
    {'left': ['up', 'left']}, 
    {'down': ['left', 'down']}, 
]

N, T = map(int, input().split())
signal = [[[] for _ in range(N)] for _ in range(N)]
visit = set()
for i in range(N):
    for j in range(N):
        for k in map(int, input().split()):
            signal[i][j].append(signal_lst[k].copy())
dfs(0, 0, 0, 'up')
print(len(visit))