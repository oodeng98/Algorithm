import sys


def subset(n, total):
    if check[0] == 1:
        return
    if 0 < n and total == 0:
        check[0] = 1
        return
    for i in range(n+1, 10):
        total += lst[i]
        subset(i, total)
        total -= lst[i]


sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T+1):
    lst = list(map(int, input().split()))
    check = [0]
    subset(0, 0)
    print(f"#{t} {check[0]}")
