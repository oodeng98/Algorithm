import sys


input = sys.stdin.readline
n = int(input())
num = int(input())
data = input().rstrip()

target = 'I' + 'OI' * n

count = 0
for i in range(num - n * 2 - 1):
    check = 1
    for j in range(2 * n + 1):
        if data[i + j] != target[j]:
            check = 0
    if check:
        count += 1
print(count)
