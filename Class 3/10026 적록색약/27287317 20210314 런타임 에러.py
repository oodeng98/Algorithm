import sys
from collections import deque
import copy


def search(photo, x, y, target):
    result = []
    photo[x][y] = 0
    if x > 0:
        if photo[x - 1][y] == target:
            result.append((x - 1, y))
    if x + 1 < len(photo):
        if photo[x + 1][y] == target:
            result.append((x + 1, y))
    if y > 0:
        if photo[x][y - 1] == target:
            result.append((x, y - 1))
    if y + 1 < len(photo[0]):
        if photo[x][y + 1] == target:
            result.append((x, y + 1))
    return result


input = sys.stdin.readline
n = int(input())
data1 = []
for i in range(n):
    temp = list(input().rstrip())
    data1.append(temp)
data2 = copy.deepcopy(data1)
already_check = [-1 for x in range(25)]
count = 0
for i in range(n * n):
    if i not in already_check:
        count += 1
        pos = (i // n, i % n)
        tar = data1[pos[0]][pos[1]]
        already_check[i] = i
        start = deque([pos])
        while start:
            temp = start.popleft()
            new = search(data1, temp[0], temp[1], tar)
            for j in new:
                already_check[j[0] * n + j[1]] = j[0] * n + j[1]
            start.extend(new)
print(count, end=' ')

for i in range(n):
    for j in range(n):
        if data2[i][j] == 'G':
            data2[i][j] = 'R'
already_check = [-1 for x in range(25)]
count = 0

for i in range(n * n):
    if i not in already_check:
        count += 1
        pos = (i // n, i % n)
        tar = data2[pos[0]][pos[1]]
        already_check[i] = i
        start = deque([pos])
        while start:
            temp = start.popleft()
            new = search(data2, temp[0], temp[1], tar)
            for j in new:
                already_check[j[0] * n + j[1]] = j[0] * n + j[1]
            start.extend(new)
print(count)