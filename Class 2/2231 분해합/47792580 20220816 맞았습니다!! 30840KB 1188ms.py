import sys

input = sys.stdin.readline
n = int(input())
# 245의 분해합은 256
# 256의 생성자는 245
result = 0
for i in range(n):
    total = i
    temp = i
    while True:
        total += temp % 10
        temp = temp // 10
        if temp < 10:
            total += temp
            break
    if total == n:
        result = 1
        break
if result:
    print(i)
else:
    print(0)
