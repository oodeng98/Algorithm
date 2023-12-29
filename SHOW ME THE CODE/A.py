import sys

input = sys.stdin.readline
N = int(input().strip())
direction = list(map(int, input().split()))
score = [0]
for i in range(N):
    if direction[i] == 1:
        score.append(score[-1] + 1)
    else:
        score.append(score[-1] - 1)
result = max(score) - min(score)
print(result)