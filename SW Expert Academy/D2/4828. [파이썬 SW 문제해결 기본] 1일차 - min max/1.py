import sys

sys.stdin = open("4828_input.txt")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min_value = float('inf')
    max_value = 0
    for i in arr:
        if min_value > i:
            min_value = i
        if max_value < i:
            max_value = i
    print(f"#{t} {max_value - min_value}")