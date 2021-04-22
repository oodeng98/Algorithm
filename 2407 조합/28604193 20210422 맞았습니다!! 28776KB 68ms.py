import sys
import itertools

input = sys.stdin.readline
n, m = map(int, input().split())
result = 1
for i in range(n, n - m, -1):
    result *= i
for i in range(1, m + 1):
    result //= i
print(result)