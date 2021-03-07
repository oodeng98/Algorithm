import sys

input = sys.stdin.readline

num1 = int(input())
data1 = input().split()
data1_dict = {}
for i in data1:
    data1_dict[i] = data1_dict.setdefault(i, 0) + 1

num2 = int(input())
data2 = input().split()
for i in data2:
    if i not in data1_dict.keys():
        print(0, end=' ')
        continue
    print(data1_dict[i], end=' ')