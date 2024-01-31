import sys


def near(a, b):
    ret = 0
    if 0 <= a - 1 < N and 0 <= b < N:
        ret += abs(arr[a-1][b] - arr[a][b])
    if 0 <= a + 1 < N and 0 <= b < N:
        ret += abs(arr[a+1][b] - arr[a][b])
    if 0 <= a < N and 0 <= b - 1 < N:
        ret += abs(arr[a][b-1] - arr[a][b])
    if 0 <= a < N and 0 <= b + 1 < N:
        ret += abs(arr[a][b+1] - arr[a][b])
    return ret


sys.stdin = open("input.txt")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    total = 0
    for i in range(N):
        for j in range(N):
            total += near(i, j)
    print(f"#{t} {total}")