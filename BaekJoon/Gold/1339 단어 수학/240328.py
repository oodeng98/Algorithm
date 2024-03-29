import sys


input = sys.stdin.readline
N = int(input())
arrange = {}

for _ in range(N):
    words = input().strip()
    power = 0
    for i in words[::-1]:
        if i in arrange:
            arrange[i] += 10 ** power
        else:
            arrange[i] = 10 ** power
        power += 1

alphabet = {}
num = 9
result = 0
temp = sorted(list(arrange.items()), key=lambda x: x[1], reverse=True)
for alpha, value in temp:
    result += num * value
    num -= 1
print(result)