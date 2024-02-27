import sys

sys.stdin = open('input.txt')


from itertools import combinations


T = int(input())
for t in range(1, T+1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    lst = [i for i in range(N//2)]
    for comb in combinations(lst, N//2):
        
        print(i)
    print(f"#{t} {0}")
    break