num = int(input())

list_data = [0 for x in range(10001)]

for i in range(num):
    list_data[int(input())] += 1

for i in range(10000):
    temp = list_data[i]
    if temp == 0:
        continue
    for j in range(temp):
        print(i)