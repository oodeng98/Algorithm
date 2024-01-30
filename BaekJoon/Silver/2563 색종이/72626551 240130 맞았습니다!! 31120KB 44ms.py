import sys

input = sys.stdin.readline

N = int(input())
paper = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            paper[x-1+i][y-1+j] = 1
count = 0
for i in paper:
    for j in i:
        if j == 1:
            count += 1
print(count)