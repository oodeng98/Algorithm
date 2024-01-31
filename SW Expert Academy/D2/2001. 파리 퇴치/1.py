import sys


def near(a, b):
    ret = 0
    if a < N - (M - 1) and b < N - (M - 1):
        for x in range(M):
            for y in range(M):
                ret += arr[a + x][b + y]
    return ret

sys.stdin = open("input.txt")

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    max_value = 0
    for i in range(N):
        for j in range(N):
            temp = near(i, j)
            if max_value < temp:
                max_value = temp
    print(f"#{t} {max_value}")
