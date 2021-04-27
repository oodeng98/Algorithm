import sys

input = sys.stdin.readline
a, b, c = map(int, input().split())
temp = a % c
remainder = [temp]
for i in range(1, 31):
    remainder.append(remainder[i-1] ** 2 % c)
data = str(bin(b))
i = len(data) - 1
j = 0
result = 1
while True:
    if data[i] == "b":
        break
    elif data[i] == "1":
        result *= remainder[j]
        result = result % c
    i -= 1
    j += 1
print(result)
# 범위는 2^31 - 1이하
