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
    remove_list = []
    for i in target:
        for j in connection:
            if j[0] == i:
                new_zombie.append(j[1])
                result.add(j[1])
                remove_list.append(j)
    target = new_zombie

print(len(result)-1)