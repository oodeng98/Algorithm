import sys


input = sys.stdin.readline
n = int(input())
coor = []
for _ in range(n):
    coor.append(list(map(int, input().split())))
coor.append(coor[0])
result = 0
for i in range(n):
    result += abs(coor[i][1] * coor[i + 1][0] - coor[i][0] * coor[i + 1][1])
print(round(result / 2, 1))
