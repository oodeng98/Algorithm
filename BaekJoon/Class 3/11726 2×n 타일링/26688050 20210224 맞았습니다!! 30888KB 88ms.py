import sys
from math import comb


input = sys.stdin.readline
num = int(input())
result = 0
for i in range(num // 2 + 1):
    result += comb(num - i, i)
print(int(result % 10007))