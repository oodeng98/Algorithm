num = int(input())
data = []
for i in range(num):
    data.append(int(input()))

dict_data = {}
for i in data:
    if i in dict_data:
        dict_data[i] += 1
    else:
        dict_data[i] = 1
result = sorted(tuple(dict_data.items()), key=lambda x: x[0])

for i in result:
    for j in range(i[1]):
        print(i[0])