import sys

sys.stdin = open('input.txt')


def delta(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        if 0 <= x + dx[i] < N and 0 <= y + dy[i] < N:
            yield x + dx[i], y + dy[i]


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_num = -float('inf')
    max_count = -float('inf')
    for i in range(N):
        for j in range(N):
            for a, b in delta(i, j):
                if arr[a][b] == arr[i][j] - 1:
                    break
            else:
                num = arr[i][j]
                count = 1
                x, y = i, j
                while True:
                    for a, b in delta(x, y):
                        if arr[a][b] == num + 1:
                            x, y = a, b
                            num += 1
                            break
                    else:
                        break
                    count += 1
                if max_count < count:
                    max_num = arr[i][j]
                    max_count = count
                elif max_count == count:
                    if arr[i][j] < max_num:
                        max_num = arr[i][j]
    print(f"#{t} {max_num} {max_count}")