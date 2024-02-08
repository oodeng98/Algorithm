import sys

sys.stdin = open('input.txt')
for t in range(1, int(input()) + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    max_value = 0
    result = 0
    for i in range(N-1, -1, -1):
        if max_value < lst[i]:
            max_value = lst[i]
        else:
            result += max_value - lst[i]
    print(f"#{t} {result}")