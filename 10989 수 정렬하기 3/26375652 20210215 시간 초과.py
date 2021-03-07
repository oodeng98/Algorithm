num = int(input())
dict_data = {}
for i in range(num):
    temp = int(input())
    dict_data[temp] = dict_data.setdefault(temp, 0) + 1

for i in sorted(tuple(dict_data.items()), key=lambda x: x[0]):
    for j in range(i[1]):
        print(i[0])