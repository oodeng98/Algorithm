from itertools import permutations
 
 
def dfs(right, left, n):
    if n == N:
        return 1
    if total <= left * 2:
        return 2 ** (N - n)
    if right + temp[n] <= left:
        return dfs(right + temp[n], left, n+1) + dfs(right, left + temp[n], n+1)
    return dfs(right, left + temp[n], n+1)
         
 
T = int(input())
for t in range(1, T+1):
    N = int(input())
    weights = list(map(int, input().split()))
    total = sum(weights)
    result = 0
    for temp in permutations(weights, N):
        result += dfs(0, temp[0], 1)
    print(f"#{t} {result}")