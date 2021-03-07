import sys


input = sys.stdin.readline
num = int(input())

for i in range(num):
    m, n, x, y = map(int, input().split())
    a = 1
    b = 1
    for j in range(1, 40002):
        a += 1
        b += 1
        if a > m:
            a = 1
        if b > n:
            b = 1
        if a == x and b == y:
            print(j+1)
            break
        if j == 40001:
            print(-1)