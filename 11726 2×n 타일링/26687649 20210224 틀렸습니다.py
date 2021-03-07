import sys


def factorial(n):
    rt = 1
    for i in range(1, n+1):
        rt *= i
    return rt


input = sys.stdin.readline
num = int(input())
result = 0
for i in range(num // 2 + 1):
    result += factorial(num - i) / (factorial(num - 2 * i) * factorial(i))
print(int(result))