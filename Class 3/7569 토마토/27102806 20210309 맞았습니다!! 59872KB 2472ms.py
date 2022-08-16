import sys


def all_direction(data, pre, n):
    result = []
    if pre[0] + n < len(data):
        if data[pre[0] + n][pre[1]] == 0:
            data[pre[0] + n][pre[1]] = 1
            result.append((pre[0] + n, pre[1]))
    if pre[0] - n >= 0:
        if data[pre[0] - n][pre[1]] == 0:
            data[pre[0] - n][pre[1]] = 1
            result.append((pre[0] - n, pre[1]))
    height = pre[0] // n
    if pre[0] + 1 < n * (height + 1) and pre[0] + 1 < len(data):
        if data[pre[0] + 1][pre[1]] == 0:
            data[pre[0] + 1][pre[1]] = 1
            result.append((pre[0] + 1, pre[1]))
    if pre[0] - 1 >= n * height:
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
perfect_tomato = []
for i in range(n * h):
    for j in range(m):
        if tomato[i][j] == 1:
            perfect_tomato.append((i, j))
count = 0
while True:
    temp = []
    for i in perfect_tomato:
        temp.extend(all_direction(tomato, i, n))

    # for i in tomato:
    #     for j in i:
    #         print(j, end=' ')
    #     print()
    # print()

    perfect_tomato = temp
    if len(temp) == 0:
        break
    count += 1

check = 0
for i in tomato:
    if 0 in i:
        check = 1
        break
if check == 1:
    print(-1)
else:
    print(count)