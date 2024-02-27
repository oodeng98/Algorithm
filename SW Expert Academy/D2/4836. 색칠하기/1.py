import sys

sys.stdin = open("input.txt")

T = int(input())
for t in range(1, T+1):
    arr = [[0 for _ in range(10)] for _ in range(10)]
    N = int(input())
    for _ in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                arr[i][j] += 1
    count = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 2:
                count += 1
    print(f"#{t} {count}")
