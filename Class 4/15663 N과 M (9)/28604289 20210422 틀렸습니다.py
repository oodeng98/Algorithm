import sys
import itertools

input = sys.stdin.readline
n, m = map(int, input().split())
n_list = sorted(list(map(int, input().split())))
if m == 1:
    for i in set(n_list):
        print(i)
else:
    result = sorted(list(set(itertools.permutations(n_list, m))))
    for i in result:
        for j in i:
            print(j, end=' ')
        print()