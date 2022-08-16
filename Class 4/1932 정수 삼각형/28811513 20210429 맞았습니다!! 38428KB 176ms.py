import sys

input = sys.stdin.readline
n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
cost = [data[0]]
index = 0
while index < n - 1:
    temp_list = []
    for i in range(index + 2):
        if i == 0:
            temp_list.append(cost[index][i] + data[index + 1][i])
        elif i == index + 1:
            temp_list.append(cost[index][i - 1] + data[index + 1][i])
        else:
            temp_list.append(max(cost[index][i-1], cost[index][i]) + data[index + 1][i])
    cost.append(temp_list)
    index += 1
print(max(cost[-1]))
