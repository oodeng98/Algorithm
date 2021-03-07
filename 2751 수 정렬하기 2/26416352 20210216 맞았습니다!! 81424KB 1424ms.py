import sys

input = sys.stdin.readline
num = int(input())

data = []
for i in range(num):
    data.append(int(input()))
for i in sorted(data):
    print(i)