import sys
import copy


def find_path(recent_check):
    if (n - 1, m - 1) in check or not recent_check:
        return 1
    new_check = set()
    for i in recent_check:
        x = i[0]
        y = i[1]
        if x + 1 < n and not mp[x + 1][y] and (x + 1, y) not in check:
            new_check.add((x + 1, y))
        if 0 <= x - 1 and not mp[x - 1][y] and (x - 1, y) not in check:
            new_check.add((x - 1, y))
        if y + 1 < m and not mp[x][y + 1] and (x, y + 1) not in check:
            new_check.add((x, y + 1))
        if 0 <= y - 1 and not mp[x][y - 1] and (x, y - 1) not in check:
            new_check.add((x, y - 1))
    for i in new_check:
        check[i] = 0
    return 1 + find_path(new_check)


sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n, m = map(int, input().split())
origin_mp = []
for i in range(n):
    temp = input().strip()
    origin_mp.append([int(x) for x in temp])

lst_1 = []
for i in range(n):
    for j in range(m):
        if origin_mp[i][j] == 1:
            lst_1.append((i, j))

results = set()
for i in lst_1:
    check = {(0, 0): 0}
    mp = copy.deepcopy(origin_mp)
    mp[i[0]][i[1]] = 0
    result = find_path([(0, 0)])
    if (n - 1, m - 1) in check:
        results.add(result)
    else:
        results.add(-1)
# print(results)
if len(results) == 1 and -1 in results:
    print(-1)
else:
    results.discard(-1)
    print(min(results))



"""
6 4
0100
1110
1000
0000
0111
0000
"""