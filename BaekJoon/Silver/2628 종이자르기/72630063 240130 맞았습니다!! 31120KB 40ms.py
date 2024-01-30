import sys

input = sys.stdin.readline

width, height = map(int, input().split())
N = int(input())

dic = {0: [0, height], 1: [0, width]} # 0은 가로, 1은 세로로 자름
for _ in range(N):
    a, b = map(int, input().split())
    dic[a].append(b)
dic[0].sort()
dic[1].sort()

result = 0
for x in range(len(dic[0]) - 1):
    for y in range(len(dic[1]) - 1):
        result = max(result, (dic[0][x+1] - dic[0][x]) * (dic[1][y+1] - dic[1][y]))
print(result)