import sys


input = sys.stdin.readline
W, N = map(int, input().split())
metal = [tuple(map(int, input().split())) for _ in range(N)]
metal.sort(key=lambda x: x[1], reverse=True)
result = 0
for weight, price in metal:
    if weight <= W:
        result += weight * price
        W -= weight
    else:
        result += W * price
        break
print(result)