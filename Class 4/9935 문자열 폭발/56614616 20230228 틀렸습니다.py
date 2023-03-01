import sys


input = sys.stdin.readline
target = str(input().rstrip())
bomb = str(input().rstrip())

bomb_dic = {}
for i in bomb:
    bomb_dic[i] = 0
length = len(bomb)

result = {}
stack = []

for index, i in enumerate(target):
    if i not in bomb_dic:
        result[index] = i
        for i in stack:
            result[i[0]] = i[1]
        stack = []
    else:
        if i == bomb[-1]:
            if len(stack) >= length - 1:
                temp = [x[1] for x in stack[-length + 1:]]
                if ''.join(temp) + i == bomb:
                    for _ in range(length - 1):
                        stack.pop()
        else:
            stack.append((index, i))

if not result:
    print("FRULA")
else:
    sequence = sorted(list(result.keys()))
    for i in sequence:
        print(result[i], end='')
