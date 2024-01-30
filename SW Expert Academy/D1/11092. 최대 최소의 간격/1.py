import sys

sys.stdin = open("sample_input.txt")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min_value = float('inf')
    min_pos = -1
    max_value = 0
    max_pos = -1
    for index, i in enumerate(arr):
        if i < min_value:
            min_value = i
            min_pos = index
        if max_value <= i:
            max_value = i
            max_pos = index
    print(f"#{t} {abs(max_pos - min_pos)}")