import sys


def charge(n, power, count):
    if n == N:
        result[0] = min(result[0], count)
        return
    if result[0] <= count:
        return
    for i in range(n+1, min(n+1+power, N+1)):
        charge(i, lst[i-1], count+1)


sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T+1):
    N, *lst = map(int, input().split())
    lst.append(0)
    result = [float('inf')]
    charge(1, lst[0], 0)
    print(f"#{t} {result[0]-1}")