import sys


input = sys.stdin.readline

K = int(input())
dic = {}
small = []
for _ in range(6):
    dir, length = map(int, input().split())
    if dir in dic:
        small.append(min(dic[dir], length))
        dic[dir] = max(dic[dir], length)
    else:
        dic[dir] = length
print(K * (max(dic[1], dic[2]) * max(dic[3], dic[4]) - small[0] * small[1]))