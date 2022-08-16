num = int(input())
dict_data = {x:0 for x in range(1, 10001)}
for i in range(num):
    temp = int(input())
    dict_data[temp] += 1

for i in dict_data.items():
    for j in range(i[1]):
        print(i[0])