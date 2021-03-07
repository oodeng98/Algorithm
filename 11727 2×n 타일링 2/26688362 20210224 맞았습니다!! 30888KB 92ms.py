import sys
from math import comb


input = sys.stdin.readline
num = int(input())
result = 0
for i in range(num // 2 + 1):  # i의 개수는 2의 개수
    result += (comb(num - i, i) % 10007) * (2 ** i) % 10007
print(int(result % 10007))