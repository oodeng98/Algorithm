num = int(input())
data = []
for i in range(num):
    data.append(input().split() + [i])
data = sorted(data, key=lambda x: (x[0], x[2]))

for i in data:
    print(i[0], i[1])