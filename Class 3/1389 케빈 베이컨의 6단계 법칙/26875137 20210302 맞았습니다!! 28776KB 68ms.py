import sys


input = sys.stdin.readline
node, line = map(int, input().split())
data = []
for i in range(line):
    data.append(tuple(map(int, input().split())))
friends = {x: [] for x in range(1, node+1)}
for i in data:
    friends[i[0]].append(i[1])
    friends[i[1]].append(i[0])
min_value = []
for i in range(1, node+1):
    total = set(friends[i])
    lst = friends[i]
    count = len(total)
    total.add(i)
    i = 2
    while len(total) < node:
        new_lst = set([])
        for j in lst:
            new_lst.update(friends[j])
        count += len(new_lst - total) * i
        total |= new_lst
        lst = new_lst
        i += 1
    min_value.append(count)
print(min_value.index(min(min_value)) + 1)