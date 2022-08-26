import sys
from heapq import heappush, heappop


input = sys.stdin.readline
n = int(input())
m = int(input())
bus = {}
for i in range(m):
    temp = list(map(int, input().split()))
    if temp[0] in bus:
        if temp[1] in bus[temp[0]]:
            bus[temp[0]][temp[1]] = min(bus[temp[0]][temp[1]], temp[2])
        else:
            bus[temp[0]][temp[1]] = temp[2]
    else:
        bus[temp[0]] = {temp[1]: temp[2]}

result = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in bus:
    for j in bus[i]:
        result[i][j] = bus[i][j]

candidate = [(x, y) for x in range(1, n + 1) for y in range(1, n + 1)]
#  bus에서 땡겨오면 안되고 result에서 땡겨와야하는데?
for i in range(1, n + 1):
    pick = []
    for j in candidate:
        if i not in j and j[0] != j[1]:
            pick.append(j)
    for j in pick:
        if result[j[0]][j[1]] > 0:
            if result[j[0]][i] > 0 and result[i][j[1]] > 0:
                result[j[0]][j[1]] = min(result[j[0]][j[1]], result[j[0]][i] + result[i][j[1]])
        else:
            if result[j[0]][i] > 0 and result[i][j[1]] > 0:
                result[j[0]][j[1]] = result[j[0]][i] + result[i][j[1]]
for i in result[1:]:
    print(' '.join([str(x) for x in i[1:]]))
