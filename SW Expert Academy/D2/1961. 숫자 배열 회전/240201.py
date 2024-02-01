import sys

sys.stdin = open("input.txt")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    print(f"#{t}")
    for i in range(N):
        result = ''
        for j in range(N):
            result += str(arr[N-1-j][i])
        result += ' '

        for j in range(N):
            result += str(arr[N-1-i][N-1-j])
        result += ' '

        for j in range(N):
            result += str(arr[j][N-1-i])
        print(result)