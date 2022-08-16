import sys


input = sys.stdin.readline
num1, num2 = input().rstrip().split()
data = {}
for i in range(int(num1)):
    temp = input().split()
    data[temp[0]] = temp[1]

for i in range(int(num2)):
    print(data[input().rstrip()])