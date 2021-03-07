import sys

input = sys.stdin.readline

num = int(input())
five = 0
for i in range(1, num+1):
    if i % 125 == 0:
        five += 3
    elif i % 25 == 0:
        five += 2
    elif i % 5 == 0:
        five += 1
print(five)