import sys

input = sys.stdin.readline

N, K = map(int, input().split())
dic = {}
for _ in range(N):
    S, Y = map(int, input().split())
    if Y in dic:
        dic[Y][S] += 1
    else:
        dic[Y] = {0: 0, 1: 0}
        dic[Y][S] += 1

result = 0
for i in dic:
    for j in dic[i]:
        if dic[i][j] % K == 0:
            result += dic[i][j] // K
        else:
            result += dic[i][j] // K + 1
print(result)