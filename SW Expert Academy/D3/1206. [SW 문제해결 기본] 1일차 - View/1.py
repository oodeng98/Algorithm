import sys

sys.stdin = open("input.txt")

T = 10
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    total = 0
    for i in range(2, N - 2):
        max_value = 0
        for j in range(-2, 3):
            if j == 0:
                continue
            if max_value < arr[i+j]:
                max_value = arr[i+j]
        if max_value > arr[i]:
            continue
        else:
            total += arr[i] - max_value
    print(f"#{t} {total}")

