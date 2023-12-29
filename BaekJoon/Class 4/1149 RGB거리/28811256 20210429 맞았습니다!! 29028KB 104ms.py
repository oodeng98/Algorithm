import sys

input = sys.stdin.readline
n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
cost = [data[0]]
index = 1
while index < n:
    temp1 = min(cost[index - 1][1], cost[index - 1][2]) + data[index][0]
    temp2 = min(cost[index - 1][0], cost[index - 1][2]) + data[index][1]
    temp3 = min(cost[index - 1][0], cost[index - 1][1]) + data[index][2]
    cost.append([temp1, temp2, temp3])
    index += 1
print(min(cost[-1]))