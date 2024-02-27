import sys

sys.stdin = open('input.txt')


def comb(n):
    if n == N-1:
        temp = 0
        last = 0
        for i in lst:
            temp += arr[last][i]
            last = i
            if battery[0] < temp:
                break
        else:
            temp += arr[last][0]
            if temp < battery[0]:
                battery[0] = temp
    else:
        for i in range(n, N-1):
            lst[n], lst[i] = lst[i], lst[n]
            comb(n+1)
            lst[n], lst[i] = lst[i], lst[n]


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = [i for i in range(1, N)]
    battery = [float('inf')]
    comb(0)
    print(f"#{t} {battery[0]}")