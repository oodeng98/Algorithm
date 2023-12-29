import sys

input = sys.stdin.readline
n = int(input())
score = []
for i in range(n):
    score.append(int(input()))

score.sort()

cutLine =  round(n * 0.15)
total_score = sum(score[cutLine: -cutLine])

if n == 0:
    print(0)
else:
    print(round(total_score / (n - cutLine * 2)))