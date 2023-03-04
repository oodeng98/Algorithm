import sys
from math import gcd


input = sys.stdin.readline
m = int(input())
result = 0
for _ in range(m):
    n, s = map(int, input().split())
    biggest = gcd(n, s)
    n = n // biggest
    s = s // biggest
    q = s * (1000000008 // n) % 1000000007
    result = (result + q) % 1000000007
print(result)
'''
2
3 7
5 9

1
15 62
'''