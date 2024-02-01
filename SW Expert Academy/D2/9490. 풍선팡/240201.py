import sys


def near(a, b):
    ret = arr[a][b]
    for i in range(1, arr[a][b]+1):
        if 0 <= a - i < N and 0 <= b < M:
            ret += arr[a-i][b]
        if 0 <= a + i < N and 0 <= b < M:
            ret += arr[a+i][b]
        if 0 <= a < N and 0 <= b - i < M:
            ret += arr[a][b-i]
        if 0 <= a < N and 0 <= b + i < M:
            ret += arr[a][b+i]
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