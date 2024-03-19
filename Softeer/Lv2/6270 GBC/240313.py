import sys


input = sys.stdin.readline
N, M = map(int, input().split())
restrict = [(0, 0)]
height = 0
for _ in range(N):
    a, b = map(int, input().split())
    height += a
    restrict.append((height, b))

test_run = []
height = 0
for _ in range(M):
    a, b = map(int, input().split())
    test_run.append((height, height + a, b))
    height += a

r_s = 0
r_t = 1
max_result = 0
for t in test_run:
    while r_s <= N:
        if t[0] < restrict[r_s+1][0]:
            break
        r_s += 1
    while r_t < M:
        if t[1] <= restrict[r_t][0]:
            break
        r_t += 1
    for i in range(r_s+1, r_t+1):
        max_result = max(max_result, max(t[2] - restrict[i][1], 0))

print(max_result)