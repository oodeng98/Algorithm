import sys

input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))

max_value = 0
for k in range(K):
    max_value += lst[k]

temp = max_value
for i in range(K, N):
    temp = temp - lst[i-K] + lst[i]
    max_value = max(max_value, temp)
print(max_value)