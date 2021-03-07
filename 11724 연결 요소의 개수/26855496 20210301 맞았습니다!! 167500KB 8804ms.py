import sys


input = sys.stdin.readline
node, line = map(int, input().split())
connection = []
for i in range(line):
    a, b = map(int, input().split())
    connection.append(set([a, b]))
while True:
    check = 0
    for i in range(len(connection) - 1):
        j = 1
        while i + j <= len(connection) - 1:
            if len(connection[i] | connection[i+j]) < len(connection[i]) + len(connection[i+j]):
                connection[i] = connection[i] | connection[i + j]
                temp = connection[i + j]
                connection[i + j] = connection[-1]
                connection[-1] = temp
                connection.pop()
                check = 1
                break
            j += 1
        if check == 1:
            break
    if check == 0:
        break
no_connection = node
for i in connection:
    no_connection -= len(i)
print(len(connection) + no_connection)