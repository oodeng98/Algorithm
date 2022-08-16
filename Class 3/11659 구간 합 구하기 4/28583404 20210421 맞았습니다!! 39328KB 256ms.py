import sys
import itertools

input = sys.stdin.readline
n, m = map(int, input().split())
n_list = list(map(int, input().split()))
sum_list = [0]
sum_list.extend(list(itertools.accumulate(n_list)))
for i in range(m):
    start, end = map(int, input().split())
    print(sum_list[end] - sum_list[start - 1])