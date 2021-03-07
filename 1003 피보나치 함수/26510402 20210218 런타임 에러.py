import sys

input = sys.stdin.readline
num = int(input())
zero = [1, 0]
one = [0, 1]
for i in range(38):
    zero.append(zero[-2] + zero[-1])
    one.append(one[-2] + one[-1])
for i in range(num):
    n = int(input())
    print(zero[n], one[n])