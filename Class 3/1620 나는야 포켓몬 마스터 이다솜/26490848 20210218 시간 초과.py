import sys

input = sys.stdin.readline

[num1, num2] = input().split()
data = {}
for i in range(int(num1)):
    data[input().split()[0]] = i + 1
for i in range(int(num2)):
    temp = input().split()
    check = 0
    try:
        print(data[temp[0]])
    except KeyError:
        print(list(data.keys())[int(temp[0]) - 1])