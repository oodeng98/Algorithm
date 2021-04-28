import sys

input = sys.stdin.readline
a, b = map(int, input().split())
count = 1
while True:
    if b == a or b == 0:
        break
    if b % 10 == 1:
        b = b // 10
    elif b % 2 == 0:
        b //= 2
    else:
        break
    count += 1
if b == a:
    print(count)
else:
    print(-1)