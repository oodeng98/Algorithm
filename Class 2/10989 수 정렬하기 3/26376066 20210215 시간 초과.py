num = int(input())
list_data = [0 for x in range(10001)]

for i in range(num):
    list_data[int(input())] += 1

for i in range(10000):
    for j in range(list_data[i]):
        print(i)