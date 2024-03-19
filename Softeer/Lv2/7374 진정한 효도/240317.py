import sys


def cal(a, b, c):
    ret = float('inf')
    for i in range(1, 4):
        temp = abs(a - i) + abs(b - i) + abs(c - i)
        ret = min(ret, temp)
    return ret

arr = [list(map(int, input().split())) for _ in range(3)]

result = float('inf')
for i in arr:
    result = min(result, cal(*i))
for i in range(3):
    result = min(result, cal(arr[0][i], arr[1][i], arr[2][i]))
print(result)