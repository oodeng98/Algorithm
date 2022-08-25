import sys


def find_path(start, des):
    check = {start: 1}
    new_check = [start]
    count = 1
    while True:
        count += 1
        next_new_check = set()
        for i in new_check:
            x = i[0]
            y = i[1]
            if x + 1 < n and (x + 1, y) not in check and origin_mp[x + 1][y] == 0:
                next_new_check.add((x + 1, y))
            if 1 <= x and (x - 1, y) not in check and origin_mp[x - 1][y] == 0:
                next_new_check.add((x - 1, y))
            if y + 1 < m and (x, y + 1) not in check and origin_mp[x][y + 1] == 0:
                next_new_check.add((x, y + 1))
            if 1 <= y and (x, y - 1) not in check and origin_mp[x][y - 1] == 0:
                next_new_check.add((x, y - 1))
        for i in next_new_check:
            check[i] = count
        if des in next_new_check or not next_new_check:
            break
        new_check = next_new_check
    return check


input = sys.stdin.readline
n, m = map(int, input().split())
origin_mp = []
for i in range(n):
    temp = input().strip()
    origin_mp.append([int(x) for x in temp])
from_start = find_path((0, 0), (n - 1, m - 1))
from_finish = find_path((n - 1, m - 1), (0, 0))
# print(from_start)
# print(from_finish)


broke = {}
for x in range(n):
    for y in range(m):
        if origin_mp[x][y] == 1:
            start_min = n * m
            finish_min = n * m
            for cand in [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]:
                if cand in from_start:
                    start_min = min(start_min, from_start[cand])
                if cand in from_finish:
                    finish_min = min(finish_min, from_finish[cand])
            if start_min == n * m or finish_min == n * m:
                continue
            broke[start_min + finish_min + 1] = (x, y)
# print(broke)
if not broke:
    if (n-1, m-1) in from_start:
        print(from_start[(n-1, m-1)])
    else:
        print(-1)
else:
    print(min(broke))

"""
6 4
0100
1110
1000
0000
0111
0000

2 1
0
0

이거 -1로 나옴 why?
broke가 아예 없으면? 맵이 그냥 0으로 된 통짜 맵이라면?
"""