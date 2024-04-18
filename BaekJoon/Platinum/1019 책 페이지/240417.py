import sys


input = sys.stdin.readline
N = input().strip()
power = len(N) - 1
count = [0 for _ in range(10)]
common = 0
temp = ['0' for _ in range(power)]
for index, i in enumerate(N):
    if index != power:
        temp[index] = i
        common += int(''.join(temp))
    for j in range(int(i)):
        count[j] += 10 ** (power - index)
    alpha = N[index+1:]
    if alpha:
        count[int(i)] += int(alpha) + 1
    else:
        count[int(i)] += 1
for i in range(1, 10):
    count[i] += common
count[0] = common

testcount = [0 for _ in range(10)]
for i in range(1, int(N) + 1):
    for j in str(i):
        testcount[int(j)] += 1
print(count)
print(testcount)
for i in count:
    print(i, end=' ')