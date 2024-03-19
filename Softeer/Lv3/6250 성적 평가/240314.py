import sys


def ranking(lst):
    temp = [(score, index) for index, score in enumerate(lst)]
    for i in range(N):
        total[i] += temp[i][0]
    temp.sort(reverse=True)
    result = [0 for _ in range(N)]
    rank = 1
    result[temp[0][1]] = rank
    count = 0
    for i in range(1, N):
        if temp[i][0] != temp[i-1][0]:
            rank += 1
            rank += count
            count = 0
        else:
            count += 1
        result[temp[i][1]] = rank
    print(' '.join(map(str, result)))


input = sys.stdin.readline
N = int(input())
total = [0 for _ in range(N)]
for _ in range(3):
    ranking(map(int, input().split()))
ranking(total)