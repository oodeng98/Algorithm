import sys

sys.stdin = open('input.txt')


T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = input().split()
    print(f"#{t}", end=' ')
    for i in range(N//2):
        print(lst[i], end=' ')
        print(lst[(N+1)//2+i], end=' ')
    if N % 2 == 1:
        print(lst[N//2])
    else:
        print()