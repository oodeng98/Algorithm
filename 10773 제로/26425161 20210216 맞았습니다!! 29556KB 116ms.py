import sys


input = sys.stdin.readline
num = int(input())
data = []
for i in range(num):
    temp = int(input())
    if temp == 0:
        data.pop(-1)
    else:
        data.append(temp)
result = 0
for i in data:
    result += i
print(result)