import sys

input = sys.stdin.readline
n, m = map(int, input().split())
n_list = list(map(int, input().split()))
for i in range(m):
    start, end = map(int, input().split())
    result = 0
    for j in range(start - 1, end):
        result += n_list[j]
    print(result)

