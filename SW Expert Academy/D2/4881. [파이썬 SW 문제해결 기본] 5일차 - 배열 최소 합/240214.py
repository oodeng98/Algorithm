import sys

sys.stdin = open('input.txt')


def comb(i):
    if i == N:
        global min_value
        temp = 0
        for index, j in enumerate(C):
            temp += arr[index][j]
            if min_value < temp:
                break
        else:
            min_value = temp
    else:
        temp = 0
        for j in range(i):
            temp += arr[j][C[j]]
            if min_value < temp:
                break
        else:
            for j in range(i, N):
                C[i], C[j] = C[j], C[i]
                comb(i+1)
                C[i], C[j] = C[j], C[i]


T = int(input().strip())
for t in range(1, T+1):
    N = int(input().strip())
    arr = [list(map(int, input().split())) for _ in range(N)]
    C = [i for i in range(N)]
    min_value = float('inf')
    comb(0)
    print(f"#{t} {min_value}")
