import sys
from itertools import combinations
from copy import deepcopy


def spread(maap):
    virus = area2
    ret = len(area2)
    while virus:
        new_virus = []
        for x, y in virus:
            for a, b in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= a < n and 0 <= b < m:
                    if maap[a][b] == 0:
                        maap[a][b] = 2
                        new_virus.append((a, b))
                        ret += 1
        virus = new_virus
    return ret


input = sys.stdin.readline
n, m = map(int, input().split())
mapping = []
for _ in range(n):
    mapping.append(list(map(int, input().split())))
area0 = []
area1 = 3
area2 = []
for i in range(n):
    for j in range(m):
        if mapping[i][j] == 0:
            area0.append((i, j))
        elif mapping[i][j] == 1:
            area1 += 1
        else:
            area2.append((i, j))
result = float('inf')
for wall in list(combinations(area0, 3)):
    temp_map = deepcopy(mapping)
    for i in wall:
        temp_map[i[0]][i[1]] = 1
    result = min(result, spread(temp_map))
    if result == 2:
        break
print(n * m - area1 - result)
