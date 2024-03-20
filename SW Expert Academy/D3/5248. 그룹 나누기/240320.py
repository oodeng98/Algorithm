import sys


sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    parent = [i for i in range(N+1)]
    group = {}
    while numbers:
        a = numbers.pop()
        b = numbers.pop()
        a, b = min(a, b), max(a, b)
        while a != parent[a]:
            a = parent[a]
        while b != parent[b]:
            b = parent[b]
        parent[b] = a
    for i in range(1, N+1):
        num = i
        while num != parent[num]:
            num = parent[num]
        parent[i] = num
    print(f"#{t} {parent.count(0) - 1 + len(set(parent)) - 1}")