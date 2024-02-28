import sys

sys.stdin = open('input.txt')


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input().split() for _ in range(N)]
    max_length = 0
    # 가로 체크
    for i in arr:
        count = 0
        for j in i:
            if j == '1':
                count += 1
            else:
                max_length = max(max_length, count)
                count = 0
        max_length = max(max_length, count)
    # 세로 체크
    for i in range(M):
        count = 0
        for j in range(N):
            if arr[j][i] == '1':
                count += 1
            else:
                max_length = max(max_length, count)
                count = 0
        max_length = max(max_length, count)
    print(f"#{t} {max_length}")