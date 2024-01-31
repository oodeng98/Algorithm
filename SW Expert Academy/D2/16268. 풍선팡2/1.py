import sys


def near(a, b):
    ret = arr[a][b]
    if 0 <= a - 1 < N and 0 <= b < M:
        ret += arr[a-1][b]
    if 0 <= a + 1 < N and 0 <= b < M:
        ret += arr[a+1][b]
    if 0 <= a < N and 0 <= b - 1 < M:
        ret += arr[a][b-1]
    if 0 <= a < N and 0 <= b + 1 < M:
        ret += arr[a][b+1]
    return ret



sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    max_value = 0
    for x in range(N):
        for y in range(M):
            temp = near(x, y)
            if max_value < temp:
                max_value = temp
    print(f"#{t} {max_value}")