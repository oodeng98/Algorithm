import sys
from collections import deque


def delta(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if 0 <= a < N and 0 <= b < N:
            if arr[a][b] == '1':
                arr[a][b] = '0'
                yield a, b


input = sys.stdin.readline
N = int(input())
result = []
length = 0
arr = [list(input().strip()) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1':
            blocks = deque([(i, j)])
            arr[i][j] = '0'
            count = 0
            while blocks:
                a, b = blocks.popleft()
                for k in delta(a, b):
                    blocks.append(k)
                count += 1
            result.append(count)
            length += 1
print(length)
result.sort()
for i in result:
    print(i)