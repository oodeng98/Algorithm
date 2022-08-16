import sys

input = sys.stdin.readline
v, e = map(int, input().split())
start = [int(input())]
data = {}
for i in range(e):
    a, b, c = map(int, input().split())
    if a in data:
        data[a].append([b, c])
    else:
        data[a] = [[b, c]]
print(data)
score = [0 for x in range(v + 1)]
while data:
    try:
        new_start = []
        for i in start:
            for j in data[i]:
                new_start.append(j[0])
            del data[i]
        print(new_start)
        start = new_start
        print(data)
    except KeyError:
        break


