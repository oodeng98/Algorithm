import sys

input = sys.stdin.readline

num1, num2 = input().rstrip().split()
data1 = {}
data2 = {}
for i in range(1, int(num1) + 1):
    temp = input().rstrip()
    data1[temp] = i
    data2[str(i)] = temp
for i in range(int(num2)):
    temp = input().rstrip()
    try:
        print(data1[temp])
    except KeyError:
        print(data2[temp])