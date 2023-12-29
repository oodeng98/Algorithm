import sys


input = sys.stdin.readline
n = int(input())
card = list(map(int, input().split()))
score = [0 for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        if card[j] % card[i] == 0:
            score[i] += 1
            score[j] -= 1

for i in score:
    print(i, end=" ")