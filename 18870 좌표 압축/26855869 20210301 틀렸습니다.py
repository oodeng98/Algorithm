import sys


input = sys.stdin.readline
num = int(input())
data = input().split()
ele = sorted(list(set(data)))
data_dict = {}
for i in range(len(ele)):
    data_dict[ele[i]] = i
for i in data:
    print(data_dict[i], end=' ')