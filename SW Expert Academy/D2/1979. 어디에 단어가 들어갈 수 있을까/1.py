import sys

sys.stdin = open("input.txt")

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    
    check_arr1 = [[0 for _ in range(N)] for _ in range(N)]
    check_arr2 = [[0 for _ in range(N)] for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            # 가로 체크
            if check_arr1[i][j] == 0:
                if arr[i][j] == 1:
                    length = 1
                    for k in range(1, N - j):
                        if arr[i][j+k] == 1:
                            length += 1
                            check_arr1[i][j+k] = 1
                        else:
                            break
                    if length == K:
                        count += 1
            # 세로 체크
            if check_arr2[j][i] == 0:
                if arr[j][i] == 1:
                    length = 1
                    for k in range(1, N - j):
                        if arr[j+k][i] == 1:
                            length += 1
                            check_arr2[j+k][i] = 1
                        else:
                            break
                    if length == K:
                        count += 1
    print(f"#{t} {count}")
