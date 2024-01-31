import sys


input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
length = 1
long_length = 1
short_length = 1
for i in range(N - 1):
    if arr[i] <= arr[i+1]:
        long_length += 1
    else:
        length = max(length, long_length)
        long_length = 1
    if arr[i+1] <= arr[i]:
        short_length += 1
    else:
        length = max(length, short_length)
        short_length = 1
print(length)