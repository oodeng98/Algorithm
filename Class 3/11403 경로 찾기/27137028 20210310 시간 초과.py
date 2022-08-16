import sys


def step2(graph):
    for i in graph:  # i번째 줄 선택
        temp = i
        for j in range(num):  # 그 줄에서 1인 요소 찾기
            if i[j] == 1:
                for k in range(num):
                    if data[j][k] == 1:  # 그 줄로 넘어가서 i번째 줄에 합쳐주기
                        temp[k] = 1

input = sys.stdin.readline
num = int(input())
data = []
for i in range(num):
    data.append(list(map(int, input().split())))

for l in range(num):
    for i in range(num):  # i번째 줄 선택
        for j in range(num):  # 그 줄에서 1인 요소 찾기
            if data[i][j] == 1:
                for k in range(num):
                    if data[j][k] == 1:  # 그 줄로 넘어가서 i번째 줄에 합쳐주기
                        data[i][k] = 1

for i in data:
    for j in i:
        print(j, end=' ')
    print()
