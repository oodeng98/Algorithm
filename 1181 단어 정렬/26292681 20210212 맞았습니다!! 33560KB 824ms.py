num = int(input())
data = []
for i in range(num):
    data.append(input())

data = sorted(list(set(data)), key=lambda x: (len(x), x))

for i in range(len(data)-1):
    print(data[i])
print(data[-1], end='')