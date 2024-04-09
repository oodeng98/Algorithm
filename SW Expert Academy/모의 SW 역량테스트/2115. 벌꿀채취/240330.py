# import sys
from itertools import combinations
 
 
def colllect():
    max_value = -float('inf')
    for i in range(N * N - M + 1):
        x1, y1 = i // N, i % N
        for j in range(i + M, N * N - M + 1):
            x2, y2 = j // N, j % N
            max_value = max(max_value, hive[x1][y1] + hive[x2][y2])
    return max_value
 
 
def select(lst):
    max_value = 0
    for i in range(1, len(lst)+1):
        for j in combinations(lst, i):
            temp = 0
            volume = C
            for k in j:
                if 0 <= volume - k:
                    temp += k ** 2
                    volume -= k
                else:
                    break
            max_value = max(max_value, temp)
    return max_value
 
 
# sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T+1):
    N, M, C = map(int, input().split())
    hive = [[] for _ in range(N)]
    for i in range(N):
        lst = list(map(int, input().split()))
        for j in range(N):
            target = lst[j:min(j+M, N)]
            hive[i].append(select(target))
    print(f"#{t} {colllect()}")