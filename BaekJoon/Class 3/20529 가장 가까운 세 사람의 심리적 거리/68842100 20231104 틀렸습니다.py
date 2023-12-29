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
    temp = input().split()
    students = {}
    for i in temp:
        if i in students:
            students[i] += 1
        else:
            students[i] = 1
    
    check = 0
    for i in students:
        if students[i] >= 3:
            result.append(0)
            check = 1
            break
    if check:
        continue
    
    all_case = itertools.combinations(students, 3)
    min_result = 12
    for i in all_case:
        a, b, c = i
        temp_result = score_graph[a][b] + score_graph[a][c] + score_graph[b][c]
        min_result = min(min_result, temp_result)
    result.append(min_result)
    
for i in result:
    print(i)

# 만약 케이스가 16개가 넘으면, 무조건 겹치는 경우가 생김
# 그러면 3개가 중복되는 경우가 있으면 무조건 0이고, 나머지의 경우만 계산해주게 하면 시간초과는 안생길듯?