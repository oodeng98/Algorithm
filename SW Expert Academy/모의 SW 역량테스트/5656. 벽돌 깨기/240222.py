import sys
import time

sys.stdin = open('input.txt')


from copy import deepcopy


def IndexCheck(x, y, n):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(1, n):
        for j in range(4):
            a, b = x + dx[j] * i, y + dy[j] * i
            if 0 <= a < W and 0 <= b < H:
                yield a, b


def Bomb(table, n):
    if n == 0:
        result = 0
        for i in table:
            for j in i:
                if j == 0:
                    break
                result += 1
        results.append(result)
        return
    for i in range(W):
        new_table = deepcopy(table)
        stack = []
        # 가장 오른쪽 벽돌 위치 찾기
        for j in range(H-1, -1, -1):
            if new_table[i][j] != 0:
                stack.append((i, j))
                break
        # 벽돌 깨기
        while stack:
            a, b = stack.pop()
            for x, y in IndexCheck(a, b, new_table[a][b]):
                stack.append((x, y))
            new_table[a][b] = 0
        # 벽돌 아래로 떨어지기
        for j in range(W):
            count = 0
            for k in range(H):
                if new_table[j][k] != 0:
                    if count == 0:
                        continue
                    new_table[j][k-count] = new_table[j][k]
                    new_table[j][k] = 0
                else:
                    count += 1
        Bomb(new_table, n-1)


T = int(input())
for t in range(1, T+1):
    N, W, H = map(int, input().split())
    bricks = [[0 for _ in range(H)] for _ in range(W)]
    for i in range(H):
        for j, value in enumerate(map(int, input().split())):
            bricks[j][H-1-i] = value
    results = []
    Bomb(bricks, N)
    print(f"#{t} {min(results)}")