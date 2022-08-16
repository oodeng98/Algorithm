import sys


input = sys.stdin.readline
num = int(input())
data = list(map(int, input().split()))
data.sort()
result = 0
for i in range(num):
    result += data[i] * (num - i)
print(result)