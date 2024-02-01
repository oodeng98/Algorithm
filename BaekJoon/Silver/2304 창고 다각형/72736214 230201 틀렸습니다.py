import sys

input = sys.stdin.readline

N = int(input())
lh = []
for _ in range(N):
    lh.append(tuple(map(int, input().split())))
lh.sort(key=lambda x: x[0])

area = 0
# 시작 값보다 큰 값을 구하면 이동
max_value = lh[0]
for i in range(1, N):
    if max_value[1] < lh[i][1]:
        area += max_value[1] * (lh[i][0] - max_value[0])
        max_value = lh[i]

# 최대 층 더해줌
area += max_value[1]
# 나보다 큰 값이 없으면 나머지에서 가장 큰 값 구하고 이동
max_value = lh[N-1]
for i in range(N-2, -1, -1):
    if max_value[1] < lh[i][1]:
        area += max_value[1] * (max_value[0] - lh[i][0])
        max_value = lh[i]
print(area)
    