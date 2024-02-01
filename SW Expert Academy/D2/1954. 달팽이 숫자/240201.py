import sys

sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    dir = {0: 1, 1: 2, 2: 3, 3: 0}
    now = 0
    a, b = 0, 0
    count = 1
    arr[a][b] = count
    count += 1
    while count <= N * N:
        if now == 0 and b + 1 < N:
            if arr[a][b+1] == 0:
                b += 1
                arr[a][b] = count
                count += 1
            else:
                now = dir[now]
        elif now == 1 and a + 1 < N:
            if arr[a+1][b] == 0:
                a += 1
                arr[a][b] = count
                count += 1
            else:
                now = dir[now]
        elif now == 2 and 0 <= b - 1:
            if arr[a][b-1] == 0:
                b -= 1
                arr[a][b] = count
                count += 1
            else:
                now = dir[now]
        elif now == 3 and 0 <= a - 1:
            if arr[a-1][b] == 0:
                a -= 1
                arr[a][b] = count
                count += 1
            else:
                now = dir[now]
        else:
            now = dir[now]
    print(f"#{t}")
    for i in arr:
        print(" ".join(map(str, i)))