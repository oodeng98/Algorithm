import sys

input = sys.stdin.readline
num = int(input())
one = [1, 0, 1]
for i in range(39):
    one.append(one[-2] + one[-1])
for i in range(num):
    n = int(input())
    print(one[n], one[n+1])