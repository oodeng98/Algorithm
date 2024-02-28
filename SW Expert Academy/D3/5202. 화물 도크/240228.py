import sys

sys.stdin = open('input.txt')


def dfs(index):
    result = []
    for i in range(index+1, N+1):
        if schedule[index][1] <= schedule[i][0]:
            result.append(dfs(i) + 1)
    if not result:
        return 0
    return max(result)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    schedule = [(0, 0)] + sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
    print(f"#{t} {dfs(0)}")