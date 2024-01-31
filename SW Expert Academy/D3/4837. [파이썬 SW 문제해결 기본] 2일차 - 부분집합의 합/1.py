import sys


def subset(lst, n):
    N = len(lst)
    result = []
    for i in range(2 ** n - 1, 2 ** N):
        temp = []
        for j in range(N):
            if i & (1<<j):
                temp.append(lst[j])
        result.append(temp)
    return result


sys.stdin = open('input.txt')

T = int(input())
A = [i for i in range(1, 13)]
for t in range(1, T+1):
    N, K = map(int, input().split())
    count = 0
    for case in subset(A, N):
        if len(case) != N:
            continue
        total = 0
        for i in case:
            total += i
        if total == K:
            count += 1
    print(f"#{t} {count}")
    break