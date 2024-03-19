import sys


input = sys.stdin.readline
N = int(input())
result = 2
for _ in range(N):
    result += result - 1
print(result**2)