import sys


input = sys.stdin.readline
num = int(input())
for i in range(num):
    data = [1, 1, 1, 2, 2]
    temp = int(input())
    for j in range(temp - 5):
        data.append(data[j] + data[j+4])
    print(data[temp-1])