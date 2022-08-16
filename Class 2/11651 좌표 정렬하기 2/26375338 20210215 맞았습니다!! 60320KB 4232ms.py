num = int(input())
data = []
for i in range(num):
    data.append(input().split())
for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = int(data[i][j])
    data[i] = tuple(data[i])
data = sorted(data, key=lambda x: (x[1], x[0]))

for i in data:
    print(i[0], i[1])
