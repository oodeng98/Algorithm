import sys


input = sys.stdin.readline
num1, num2 = input().rstrip().split()
data1 = set()
data2 = set()
for i in range(int(num1)):
    data1.add(input().rstrip())
for i in range(int(num2)):
    data2.add(input().rstrip())

result = list(data1 & data2)

print(len(result))
for i in sorted(result):
    print(i)