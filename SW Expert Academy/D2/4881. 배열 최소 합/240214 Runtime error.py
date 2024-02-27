import sys

sys.stdin = open('input.txt')


def comb(i):
    if i == N:
        sequence.append(tuple(C))
    else:
        for j in range(i, N):
            C[i], C[j] = C[j], C[i]
            comb(i+1)
            C[i], C[j] = C[j], C[i]


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    C = [i for i in range(N)]
    sequence = []
    comb(0)
    min_value = float('inf')
    for i in sequence:
        temp = 0
        for index, j in enumerate(i):
            temp += arr[index][j]
            if min_value < temp:
                break
        if temp < min_value:
            min_value = temp
    print(f"#{t} {min_value}")