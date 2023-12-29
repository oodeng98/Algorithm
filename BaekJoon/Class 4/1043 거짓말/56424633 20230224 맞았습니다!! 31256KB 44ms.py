import sys


input = sys.stdin.readline
n, m = map(int, input().split())
temp = list(map(int, input().split()))
passed = set(temp[1:])
people_party = {}
graph = {}
for index in range(m):
    temp = list(map(int, input().split()))
    for i in temp[1:]:
        if i in people_party:
            people_party[i].add(index)
        else:
            people_party[i] = {index}
    for i in range(temp[0]):
        for j in range(i, temp[0]):
            if temp[i + 1] in graph:
                graph[temp[i + 1]].add(temp[j + 1])
            else:
                graph[temp[i + 1]] = {temp[j + 1]}
            if temp[j + 1] in graph:
                graph[temp[j + 1]].add(temp[i + 1])
            else:
                graph[temp[j + 1]] = {temp[i + 1]}

truth = passed
while True:
    new = set()
    for people in truth:
        if people not in graph:
            continue
        for p in graph[people]:
            new.add(p)
    if len(new - truth) == 0:
        break
    passed = passed | new
    truth = new

cant = set()
for people in passed:
    if people not in people_party:
        continue
    cant = cant.union(people_party[people])

print(m - len(cant))
