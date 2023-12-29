import sys
import copy

input = sys.stdin.readline
n = int(input())
arr_max = []
arr_min = []

for i in range(n):
    temp_max = list(map(int, input().split()))
    temp_min = copy.deepcopy(temp_max)

    if i == 0:
        arr_max = temp_max
        arr_min = temp_min
        continue

    temp_max[0] += max(arr_max[0], arr_max[1])
    temp_max[1] += max(arr_max[0], arr_max[1], arr_max[2])
    temp_max[2] += max(arr_max[1], arr_max[2])
    arr_max = temp_max

    temp_min[0] += min(arr_min[0], arr_min[1])
    temp_min[1] += min(arr_min[0], arr_min[1], arr_min[2])
    temp_min[2] += min(arr_min[1], arr_min[2])
    arr_min = temp_min

print(max(arr_max), min(arr_min))
