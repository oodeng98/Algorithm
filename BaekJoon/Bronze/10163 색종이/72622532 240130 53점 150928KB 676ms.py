import sys

input = sys.stdin.readline

N = int(input())
temp = []
for _ in range(N):
    temp_set = set()
    a, b, c, d = map(int, input().split())
    for i in range(a, a + c):
        for j in range(b, b + d):
            temp_set.add((i, j))
    temp.append(temp_set)
for i in range(N):
    for j in range(i+1, N):
        temp[i] -= temp[j]
for i in temp:
    print(len(i))