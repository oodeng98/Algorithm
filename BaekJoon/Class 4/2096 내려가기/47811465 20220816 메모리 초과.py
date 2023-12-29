import sys
import copy

input = sys.stdin.readline
n = int(input())
arr_max = []

for i in range(n):
    temp = list(map(int, input().split()))
    arr_max.append(temp)

arr_min = copy.deepcopy(arr_max)

if n == 1:
    print(max(arr_max[0]), min(arr_max[0]))
else:
    for i in range(1, n):
        arr_max[i][0] += max(arr_max[i - 1][0], arr_max[i - 1][1])
        arr_max[i][1] += max(arr_max[i - 1][0], arr_max[i - 1][1], arr_max[i - 1][2])
        arr_max[i][2] += max(arr_max[i - 1][1], arr_max[i - 1][2])

        arr_min[i][0] += min(arr_min[i - 1][0], arr_min[i - 1][1])
        arr_min[i][1] += min(arr_min[i - 1][0], arr_min[i - 1][1], arr_min[i - 1][2])
        arr_min[i][2] += min(arr_min[i - 1][1], arr_min[i - 1][2])

print(max(arr_max[-1]), min(arr_min[-1]))

