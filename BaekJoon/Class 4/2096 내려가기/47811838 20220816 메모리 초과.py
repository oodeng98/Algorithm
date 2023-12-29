import sys
import copy

input = sys.stdin.readline
n = int(input())
arr_max = []

for i in range(n):
    temp = list(map(int, input().split()))
    arr_max.append(temp)

arr_min = copy.deepcopy(arr_max)

while len(arr_max) != 1:
    arr_max[1][0] += max(arr_max[0][0], arr_max[0][1])
    arr_max[1][1] += max(arr_max[0][0], arr_max[0][1], arr_max[0][2])
    arr_max[1][2] += max(arr_max[0][1], arr_max[0][2])

    arr_min[1][0] += min(arr_min[0][0], arr_min[0][1])
    arr_min[1][1] += min(arr_min[0][0], arr_min[0][1], arr_min[0][2])
    arr_min[1][2] += min(arr_min[0][1], arr_min[0][2])
    del arr_max[0], arr_min[0]

print(max(arr_max[-1]), min(arr_min[-1]))

