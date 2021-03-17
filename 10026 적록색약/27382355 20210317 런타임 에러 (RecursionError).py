import sys
import copy


def search(photo, x, y, target):
    result = []
    photo[x][y] = 0
    if x - 1 >= 0:  # up
        if photo[x - 1][y] == target:
            result.append((x - 1, y))
            result.extend(search(photo, x - 1, y, target))
    if x + 1 <= len(photo) - 1:  # down
        if photo[x + 1][y] == target:
            result.append((x + 1, y))
            result.extend(search(photo, x + 1, y, target))
    if y - 1 >= 0:  # left
        if photo[x][y - 1] == target:
            result.append((x, y - 1))
            result.extend(search(photo, x, y - 1, target))
    if y + 1 <= len(photo[0]) - 1:  # right
        if photo[x][y + 1] == target:
            result.append((x, y + 1))
            result.extend(search(photo, x, y + 1, target))
    return result


input = sys.stdin.readline
n = int(input())
data1 = []
for i in range(n):
    temp = list(input().rstrip())
    data1.append(temp)
data2 = copy.deepcopy(data1)
already_check = [1 for x in range(n * n)]
count = 0
for i in range(n * n):
    if already_check[i]:
        count += 1
        pos = (i // n, i % n)
        already_check[i] = 0
        for j in search(data1, pos[0], pos[1], data1[pos[0]][pos[1]]):
            already_check[j[0] * n + j[1]] = 0
print(count, end=' ')

for i in range(n):
    for j in range(n):
        if data2[i][j] == 'G':
            data2[i][j] = 'R'
already_check = [1 for x in range(n * n)]
count = 0

for i in range(n * n):
    if already_check[i]:
        count += 1
        pos = (i // n, i % n)
        already_check[i] = 0
        for j in search(data2, pos[0], pos[1], data2[pos[0]][pos[1]]):
            already_check[j[0] * n + j[1]] = 0
print(count)
