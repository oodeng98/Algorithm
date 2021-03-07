import sys


input = sys.stdin.readline
num1, num2 = input().rstrip().split()
data = []
result = []
for i in range(int(num1)):
    data.append(input().rstrip())
for i in range(int(num2)):
    temp = input().rstrip()
    if temp in data:
        result.append(temp)

print(len(result))
for i in sorted(result):
    print(i)