# import sys
def turn(r, c, s, arr):
    arr_copy = [i[:] for i in arr]
    r -= 1
    c -= 1
    for i in range(1, s + 1):
        pre = arr_copy[r - i][c - i]
        for j in range(c - i, c + i + 1):
            arr_copy[r - i][j], pre = pre, arr_copy[r - i][j]
        for j in range(r - i + 1, r + i + 1):
            arr_copy[j][c + i], pre = pre, arr_copy[j][c + i]
        for j in range(c + i - 1, c - i - 1, -1):
            arr_copy[r + i][j], pre = pre, arr_copy[r + i][j]
        for j in range(r + i - 1, r - i - 1, -1):
            arr_copy[j][c - i], pre = pre, arr_copy[j][c - i]
    return arr_copy


def dfs(n, arr):
    if n == K:
        for i in arr:
            min_value[0] = min(min_value[0], sum(i))
        return
    for i in range(K):
        if visited[i]:
            continue
        visited[i] = 1
        dfs(n + 1, turn(*turn_list[i], arr))
        visited[i] = 0


# input = sys.stdin.readline
N, M, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
turn_list = [list(map(int, input().split())) for _ in range(K)]

min_value = [float('inf')]
visited = [0 for _ in range(K)]
dfs(0, arr)
print(min_value[0])