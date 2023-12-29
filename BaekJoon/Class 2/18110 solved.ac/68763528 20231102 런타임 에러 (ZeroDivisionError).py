import sys

input = sys.stdin.readline
n = int(input())
score = []
for i in range(n):
    score.append(int(input()))

score.sort()

cutLine =  round(n * 0.15)
total_score = sum(score[cutLine: -cutLine])
print(round(total_score / (n - cutLine * 2)))