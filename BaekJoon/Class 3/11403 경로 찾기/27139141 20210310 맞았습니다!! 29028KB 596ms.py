import sys


def step2(line):
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

i = 0
while True:
    origin = data[i].copy()
    one = []
    for j in range(num):
        if data[i][j] == 1:
            one.append(j)
    for j in one:
        for k in range(num):
            data[i][k] = max(data[i][k], data[j][k])
    if origin == data[i]:
        i += 1
    if i == num:
        break

for i in data:
    for j in i:
        print(j, end=' ')
    print()
