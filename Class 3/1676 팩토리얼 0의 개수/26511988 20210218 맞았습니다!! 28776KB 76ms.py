import sys

input = sys.stdin.readline

num = int(input())
five = 0
for i in range(0, num+1, 5):
    if i == 0:
        continue
    if i % 125 == 0:
        five += 3
    elif i % 25 == 0:
        five += 2
    elif i % 5 == 0:
        five += 1
print(five)