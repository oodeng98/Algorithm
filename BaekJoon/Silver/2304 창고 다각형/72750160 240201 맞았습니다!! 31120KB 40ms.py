import sys

input = sys.stdin.readline

N = int(input())
lh = []
for _ in range(N):
    lh.append(tuple(map(int, input().split())))

lh.sort(key=lambda x: x[0])
max_height = max(lh, key=lambda x: x[1])

area = 0
left = 0
right = N - 1
height = 1
while height <= max_height[1]:
    if lh[left][1] < height:
        left += 1
        continue
    if lh[right][1] < height:
        right -= 1
        continue
    area += lh[right][0] + 1 - lh[left][0]
    height += 1

print(area)