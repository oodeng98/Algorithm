import sys

input = sys.stdin.readline

[num1, num2] = input().split()
data = []
for i in range(int(num1)):
    data.extend(input().split())
for i in range(int(num2)):
    temp = input().split()
    if temp[0] in data:
        print(data.index(temp[0]) + 1)
    else:
        print(data[int(temp[0]) - 1])