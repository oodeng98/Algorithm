data = input().split()
for i in range(len(data)):
    data[i] = int(data[i])

result = 1
for i in range(data[1]):
    result *= (data[0] - i) / (data[1] - i)

print(int(result))