import sys


input = sys.stdin.readline
num = int(input())

for i in range(num):
    m, n, x, y = map(int, input().split())
    a = 1
    b = 1
    if abs(x - y) % 2 == 1 and n % 2 == 0:
        print(-1)
        continue
    while (n * b + y - x) % m != 0:
        b += 1
    print(n * b + y)