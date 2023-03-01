import sys


input = sys.stdin.readline
target = str(input().rstrip())
bomb = str(input().rstrip())

bomb_dic = {}
for index, i in enumerate(bomb):
    bomb_dic[i] = index
length = len(bomb)

result = 0
stack = []

for i in target:
    if i not in bomb_dic:
        result = 1
        print(''.join(stack), end='')
        print(i, end='')
        stack = []
    else:
        if i == bomb[-1]:
            if len(stack) >= length - 1:
                if ''.join(stack[-length + 1:]) + i == bomb:
                    for _ in range(length - 1):
                        stack.pop()
        else:
            stack.append(i)

if not result:
    print("FRULA")
