import sys

input = sys.stdin.readline

N, M = map(int, input().split())
T = int(input())
pos = []
coor = []
dic = {1: 2, 2: 1, 3: 4, 4: 3}
result = 0

for t in range(T+1):
    a, b = map(int, input().split())
    pos.append((a, b))
    if a == 1:
        x, y = 0, b
    elif a == 2:
        x, y = M, b
    elif a == 3:
        x, y = b, 0
    elif a == 4:
        x, y = b, N
    coor.append((x, y))

d, _ = pos.pop()
x, y = coor.pop()


for i in range(T):
    p, _ = pos[i]
    a, b = coor[i]
    if p == dic[d]:
        if p in [1, 2]:
            result += M + min(y + b, (N - y) + (N - b))
        else:
            result += N + min(x + a, (M - x) + (M - a))
    else:
        result += abs(x - a) + abs(y - b)

print(result)
