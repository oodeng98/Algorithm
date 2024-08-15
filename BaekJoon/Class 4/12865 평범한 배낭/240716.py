import sys


input = sys.stdin.readline

N, K = map(int, input().split())
dp = [0 for _ in range(K+1)]
products = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    weight, value = products[i]
    for j in range(K, weight - 1, -1):
        dp[j] = max(dp[j], dp[j - weight] + value)
print(dp[-1])