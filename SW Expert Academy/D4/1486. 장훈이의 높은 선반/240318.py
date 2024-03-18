import sys


def subset(n):
    min_value = float('inf')
    for i in range(2 ** n):
        result = 0
        for j in range(n):
            if i & (1 << j):
                result += lst[j]
                if B <= result:
                    break
        if B <= result:
            min_value = min(min_value, result - B)
    return min_value


sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    print(f"#{t} {subset(N)}")