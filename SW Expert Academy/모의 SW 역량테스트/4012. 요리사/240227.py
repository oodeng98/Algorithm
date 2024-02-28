import sys

sys.stdin = open('input.txt')


from itertools import combinations


T = int(input())
for t in range(1, T+1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    lst = list(combinations([i for i in range(N)], N//2))
    result = float('inf')
    for i in range(len(lst) // 2):
        food1 = lst[i]
        food2 = lst[-(i+1)]
        score1 = 0
        score2 = 0
        for i in range(N//2):
            for j in range(i+1, N//2):
                a1, b1 = food1[i], food1[j]
                a2, b2 = food2[i], food2[j]
                score1 += synergy[a1][b1] + synergy[b1][a1]
                score2 += synergy[a2][b2] + synergy[b2][a2]
        result = min(result, abs(score1 - score2))
    print(f"#{t} {result}")