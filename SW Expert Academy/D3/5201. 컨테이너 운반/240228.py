import sys

sys.stdin = open('input.txt')


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    freight = sorted(list(map(int, input().split())), reverse=True  )
    truck = sorted(list(map(int, input().split())), reverse=True)
    result = 0
    f = 0
    tr = 0
    while f < N and tr < M:
        if freight[f] <= truck[tr]:
            result += freight[f]
            f += 1
            tr += 1
            continue
        f += 1
    print(f"#{t} {result}")