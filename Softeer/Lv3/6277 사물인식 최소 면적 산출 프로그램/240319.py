import sys


def square(lst):
    max_x = -float('inf')
    max_y = -float('inf')
    min_x = float('inf')
    min_y = float('inf')
    for x, y in lst:
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        min_x = min(min_x, x)
        min_y = min(min_y, y)
    return (max_x - min_x) * (max_y - min_y)

def combi(n):
    if n == K:
        result[0] = min(result[0], square(candidate))
        return
    if 4 <= n and result[0] <= square(candidate):
        return
    for i in color[n]:
        candidate.append(i)
        combi(n+1)
        candidate.pop()


input = sys.stdin.readline
N, K = map(int, input().split())
color = [[] for _ in range(K)]
for _ in range(N):
    x, y, k = map(int, input().split())
    color[k-1].append((x, y))
candidate = []
result = [float('inf')]
combi(0)
print(result[0])