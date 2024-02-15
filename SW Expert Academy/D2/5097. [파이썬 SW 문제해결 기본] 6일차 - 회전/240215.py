import sys

sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    lst = input().split()
    temp = M % N
    print(f"#{t} {lst[temp]}")