import sys

sys.stdin = open("input.txt")


T = int(input())
for t in range(1, T+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    # 가로 체크
    for i in range(N):
        height = arr[i][0]
        j = 1
        check = 0
        flat = 1
        while j < N:
            if height == arr[i][j]:
                flat += 1
                j += 1
            else:
                if abs(height - arr[i][j]) != 1:
                    break
                if height < arr[i][j]:
                    if X <= flat:
                        height = arr[i][j]
                        j += 1
                        flat = 1
                    else:
                        break
                else:
                    for k in range(1, X):
                        if N <= j + k or arr[i][j] != arr[i][j+k]:
                            check = 1
                            break
                    else:
                        height = arr[i][j]
                        j += X
                        flat = 0
                    if check:
                        break
        else:
            count += 1
    # 세로 체크
    for i in range(N):
        height = arr[0][i]
        j = 1
        check = 0
        flat = 1
        while j < N:
            if height == arr[j][i]:
                flat += 1
                j += 1
            else:
                if abs(height - arr[j][i]) != 1:
                    break
                if height < arr[j][i]:
                    if X <= flat:
                        height = arr[j][i]
                        j += 1
                        flat = 1
                    else:
                        break
                else:
                    for k in range(1, X):
                        if N <= j + k or arr[j][i] != arr[j+k][i]:
                            check = 1
                            break
                    else:
                        height = arr[j][i]
                        j += X
                        flat = 0
                    if check:
                        break
        else:
            count += 1
    print(f"#{t} {count}")