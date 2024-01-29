import sys

# sys.stdin = open("4835_input.txt")

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    min_value = float('inf')
    max_value = 0
    for n in range(N - M + 1):
        temp_value = 0
        for m in range(M):
            temp_value += arr[n + m]
        min_value = min(min_value, temp_value)
        max_value = max(max_value, temp_value)
    print(f"#{t} {max_value - min_value}")
