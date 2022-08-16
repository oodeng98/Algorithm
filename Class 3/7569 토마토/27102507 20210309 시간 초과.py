import sys


def all_direction(data, pre, n):
    result = []
    if pre[0] + h < len(data):
        if data[pre[0] + h][pre[1]] == 0:
            data[pre[0] + h][pre[1]] = 1
            result.append((pre[0] + h, pre[1]))
    if pre[0] - h >= 0:
        if data[pre[0] - h][pre[1]] == 0:
            data[pre[0] - h][pre[1]] = 1
            result.append((pre[0] - h, pre[1]))
    height = pre[0] // n
    if pre[0] + 1 < pre[0] * (height + 1) and pre[0] + 1 < len(data):
        if data[pre[0] + 1][pre[1]] == 0:
            data[pre[0] + 1][pre[1]] = 1
            result.append((pre[0] + 1, pre[1]))
    if pre[0] - 1 >= pre[0] * height:
        if data[pre[0] - 1][pre[1]] == 0:
            data[pre[0] - 1][pre[1]] = 1
            result.append((pre[0] - 1, pre[1]))
    if pre[1] + 1 < len(data[0]):
        if data[pre[0]][pre[1] + 1] == 0:
            data[pre[0]][pre[1] + 1] = 1
            result.append((pre[0], pre[1] + 1))
    if pre[1] - 1 >= 0:
        if data[pre[0]][pre[1] - 1] == 0:
            data[pre[0]][pre[1] - 1] = 1
            result.append((pre[0], pre[1] - 1))
    return result


input = sys.stdin.readline
m, n, h = map(int, input().split())
tomato = []
for i in range(h):
    for j in range(n):
        tomato.append(list(map(int, input().split())))
perfect_tomato = set()
for i in range(n * h):
    for j in range(m):
        if tomato[i][j] == 1:
            perfect_tomato.add((i, j))
count = 0
while True:
    new_perfect_tomato = set()
    for i in perfect_tomato:
        new_perfect_tomato.update(all_direction(tomato, i, n))
    new_perfect_tomato -= perfect_tomato
    perfect_tomato |= new_perfect_tomato
    if len(new_perfect_tomato) == 0:
        break
    count += 1
total = m * n * h
for i in tomato:
    for j in i:
        if j == -1:
            total -= 1
if len(perfect_tomato) != total:
    print(-1)
else:
    print(count)