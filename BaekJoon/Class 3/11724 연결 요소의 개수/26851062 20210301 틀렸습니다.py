import sys


input = sys.stdin.readline
node, line = map(int, input().split())
connection = []
for i in range(line):
    check = 0
    a, b = map(int, input().split())
    for j in connection:
        if a in j or b in j:
            j.add(a)
            j.add(b)
            check = 1
            break
    if check == 0:
        new = set([a, b])
        connection.append(new)
while True:
    before = len(connection)
    for i in range(before-1):
        if len(connection[i] | connection[i+1]) < len(connection[i]) + len(connection[i+1]):
            connection[i] = connection[i] | connection[i+1]
            connection.pop(i+1)
            break
    if before == len(connection):
        break
print(len(connection))