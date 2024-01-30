import sys

sys.stdin = open('4831_input.txt')

T = int(input())
for t in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    start = 0
    count = 0
    for i in range(M):
        for j in range(i, M):
            if arr[j] - start > K:
                break
            des = arr[j]
        start = des
        count += 1
        if N - start <= K:
            break
    if N - start > K:
        print(f"#{t} {0}")
    else:
        print(f"#{t} {count}")

