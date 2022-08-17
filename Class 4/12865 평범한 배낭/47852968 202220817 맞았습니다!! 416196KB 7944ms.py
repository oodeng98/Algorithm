import sys

input = sys.stdin.readline
n, k = map(int, input().split())

arr = []
for i in range(n):
    arr.append(tuple(map(int, input().split())))
arr.sort(key=lambda x: x[0])

dp = []
for i in range(n + 1):
    dp.append([0 for x in range(k + 1)])

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if arr[i-1][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-arr[i-1][0]] + arr[i-1][1], dp[i-1][j])

print(dp[n][k])