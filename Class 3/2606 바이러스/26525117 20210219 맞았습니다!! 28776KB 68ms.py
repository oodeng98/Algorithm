import sys

input = sys.stdin.readline

num = int(input())
n = int(input())
connection = []
for i in range(n):
    temp = input().split()
    connection.append((int(temp[0]), int(temp[1])))

target = [1]
result = {1}

while True:
    if len(target) == 0:
        break
    new_zombie = []
    remove_list = set()
    for i in target:
        for j in connection:
            if j[0] == i:
                new_zombie.append(j[1])
                result.add(j[1])
                remove_list.add(j)
            elif j[1] == i:
                new_zombie.append(j[0])
                result.add(j[0])
                remove_list.add(j)
    for i in remove_list:
        try:
            connection.remove(i)
        except ValueError:
            continue
    target = new_zombie

print(len(result)-1)