import sys

sys.stdin = open("input.txt")
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    if N % 2:
        result = -arr[N//2][N//2]
    else:
        result = 0
    for i in range(N):
        result += arr[i][i]
        result += arr[i][N-i-1]
    print(f"#{t} {result}")