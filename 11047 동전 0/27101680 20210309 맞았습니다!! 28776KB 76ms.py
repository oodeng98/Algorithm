import sys


input = sys.stdin.readline
n, target = map(int, input().split())
data = []
for i in range(n):
    data.append(int(input()))
result = 0
while True:
    big = 0
    for i in data:
        if big < i <= target:
            big = i
        if target <= i:
            break
    result += target // big
    target -= (target // big) * big
    if target == 0:
        break
print(result)


