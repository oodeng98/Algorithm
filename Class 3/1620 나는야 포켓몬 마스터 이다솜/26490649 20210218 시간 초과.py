import sys

input = sys.stdin.readline

[num1, num2] = input().split()
data = []
for i in range(int(num1)):
    data.extend(input().split())
for i in range(int(num2)):
    temp = input().split()
    check = 0
    for j in range(int(num1)):
        if data[j] == temp[0]:
            print(j+1)
            check = 1
            break
    if check == 0:
        print(data[int(temp[0]) - 1])