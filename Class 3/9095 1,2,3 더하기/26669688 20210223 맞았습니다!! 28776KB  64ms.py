import sys


def factorial(n):
    temp = 1
    for i in range(1, n+1):
        temp *= i
    return temp


input = sys.stdin.readline
num = int(input())
data = []
for i in range(num):
    data.append(int(input()))
for i in data:
    pair = []
    result = 0
    for j in range(i + 1):
        for k in range(i // 2 + 1):
            for l in range(i // 3 + 1):
                if j + 2 * k + 3 * l == i:
                    # print(f'1이 {j}개, 2가 {k}개, 3이 {l}개 있는 식이 존재한다.')
                    pair.append((j, k, l))
    for j in pair:
        result += factorial(j[0] + j[1] + j[2]) / (factorial(j[0]) * factorial(j[1]) * factorial(j[2]))
    print(int(result))