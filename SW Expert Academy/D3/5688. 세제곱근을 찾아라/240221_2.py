import sys

sys.stdin = open('input.txt')


T = int(input())
for t in range(1, T+1):
    N = int(input())
    start = 1
    end = N
    result = -1
    while start <= end:
        target = (start * 3 + end) // 4
        if target ** 3 == N:
            result = target
            break
        if target ** 3 < N:
            start = target + 1
        else:
            end = target - 1
        i = N // 4

    print(f"#{t} {result}")