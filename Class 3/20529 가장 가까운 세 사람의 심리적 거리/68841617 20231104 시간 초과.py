import sys
import itertools


def mental_distance(a, b):
    score = 0
    for i in range(4):
        if a[i] != b[i]:
            score += 1
    return score

input = sys.stdin.readline
t = int(input())

case = []
num = 0
for first in ["E", "I"]:
    for second in ["S", "N"]:
        for third in ["T", "F"]:
            for fourth in ["J", "P"]:
                case.append(first + second + third + fourth)

score_graph = {}
for i in case:
    score_graph[i] = {}
    for j in case:
        score_graph[i][j] = mental_distance(i, j)                        

result = []
for _ in range(t):
    n = int(input())
    students = input().split()
    all_case = itertools.combinations(students, 3)
    min_result = 12
    for i in all_case:
        a, b, c = i
        temp_result = score_graph[a][b] + score_graph[a][c] + score_graph[b][c]
        min_result = min(min_result, temp_result)
    result.append(min_result)
    
for i in result:
    print(i)
