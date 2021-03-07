import sys


input = sys.stdin.readline
num1, num2 = input().rstrip().split()
data1 = []
data2 = []
for i in range(int(num1)):
    data1.append(input().rstrip())
for i in range(int(num2)):
    data2.append(input().rstrip())
result = []
for i in data1:
    if i in data2:
        result.append(i)

print(len(result))
for i in sorted(result):
    print(i)