import sys
import itertools

input = sys.stdin.readline
n, m = map(int, input().split())
if m == 1:
    for i in range(1, n + 1):
        print(i)
else:
    result = list(itertools.combinations_with_replacement(range(1, n+1), m))
    for i in result:
        for j in i:
            print(j, end=' ')
        print()