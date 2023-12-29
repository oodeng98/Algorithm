import sys

input = sys.stdin.readline

num1, num2 = input().rstrip().split()
data = {}
for i in range(1, int(num1) + 1):
    data[input().rstrip()] = i
for i in range(int(num2)):
    temp = input().rstrip()
    try:
        print(data[temp])
    except KeyError:
        print(list(data.keys())[int(temp[0]) - 1])