import sys


def subset(lst, n):
    result = 0
    for i in range(2 ** n - 1, 2 ** 12):
        total = 0
        count = 0
        for j in range(12):
            if i & (1<<j):
                count += 1
                if count >= n + 1:
                    break
                total += lst[j]
                if total > K:
                    break
        if count == n and total == K:
            result += 1
    return result


sys.stdin = open('input.txt')

T = int(input())
A = [i for i in range(1, 13)]
for t in range(1, T+1):
    N, K = map(int, input().split())
    count = subset(A, N)
    print(f"#{t} {count}")