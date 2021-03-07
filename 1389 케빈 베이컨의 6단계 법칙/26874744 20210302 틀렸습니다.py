import sys


input = sys.stdin.readline
node, line = map(int, input().split())
data = []
for i in range(line):
    data.append(tuple(map(int, input().split())))
count = {x: 0 for x in range(1, node+1)}
for i in data:
    for j in i:
        count[j] += 1
big = 0
big_index = 0
for i in count:
    if big < count[i]:
        big = count[i]
        big_index = i
print(big_index)