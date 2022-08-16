import sys


input = sys.stdin.readline
num = int(input())
for i in range(num):
    closet = {}
    n = int(input())
    for j in range(n):
        a, key = input().split()
        closet[key] = closet.setdefault(key, 0) + 1
    result = 1
    for j in closet:
        result *= (closet[j] + 1)
    print(result - 1)