import sys

input = sys.stdin.readline

N = int(input())
area = [[0 for _ in range(1001)] for _ in range(1001)]
for n in range(1, N + 1):
    a, b, c, d = map(int, input().split())
    for i in range(a, a + c):
        for j in range(b, b + d):
            area[i][j] = n
result = [0 for _ in range(N+1)]
for i in area:
    for j in i:
        result[j] += 1
for i in range(1, N + 1):
    print(result[i])