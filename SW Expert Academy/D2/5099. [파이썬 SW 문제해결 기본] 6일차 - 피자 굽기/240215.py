import sys

sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    pit = [[0, 0] for _ in range(N)]
    index = 0
    while index < M:
        for i in range(N):
            pit[i][0] //= 2
            if M <= index:
                continue
            if pit[i][0] == 0:
                pit[i] = [pizza[index], index]
                index += 1
    result = -1
    while True:
        count = 0
        for i in range(N):
            if pit[i][0] != 0:
                pit[i][0] //= 2
                result = pit[i][1]
            else:
                count += 1
        if N - 1 <= count:
            break
    print(f"#{t} {result+1}")
    