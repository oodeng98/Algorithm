import sys


def subset(n, length, total):
    if length == N:
        if total == K:
            result[0] += 1
        return
    if K <= total:
        return
    for i in range(n, 12):
        total += A[i]
        subset(i+1, length+1, total)
        total -= A[i]


sys.stdin = open('input.txt')
T = int(input())
A = [i for i in range(1, 13)]
for t in range(1, T+1):
    N, K = map(int, input().split())
    result = [0]
    subset(0, 0, 0)
    print(f"#{t} {result[0]}")