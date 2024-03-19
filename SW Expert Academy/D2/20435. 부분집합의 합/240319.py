import sys


def subset(n, total):
    if total == 0:
        count[0] += 1
    for i in range(n, 10):
        total += lst[i]
        subset(i+1, total)
        total -= lst[i]


sys.stdin = open('input.txt')
lst = list(map(int, input().split()))
count = [0]
subset(0, 0)
print(f"#{1} {count[0]}")