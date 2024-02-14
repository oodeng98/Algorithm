import sys

sys.stdin = open('input.txt')


T = int(input())
for t in range(1, T+1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    path = [0 for _ in range(200)]
    for start, end in numbers:
        if start < end:
            s = start
            e = end
        else:
            s = end
            e = start
        if s % 2 == 0:
            s -= 1
        if e % 2 == 0:
            e -= 1
        s //= 2
        e //= 2
        for i in range(s, e+1):
            path[i] += 1
    max_value = 0
    for i in path:
        if max_value < i:
            max_value = i
    print(f'#{t} {max_value}')
