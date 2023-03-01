import sys


input = sys.stdin.readline
n = int(input())
m = int(input())
data = input().rstrip()

target = 'IOI'
count = []
check = 0
index = 0
while index < m:
    if data[index: index + 3] == 'IOI':
        index += 2
        check += 1
    else:
        index += 1
        if check:
            count.append(check)
            check = 0
ret = 0
for i in count:
    ret += max(0, i - n + 1)
print(ret)