num = int(input())
data = []
for i in range(num):
    data.append(input().split())

data = sorted(data, key=lambda x: x[0])

for i in data:
    print(i[0], i[1])