import sys


input = sys.stdin.readline
target = str(input().rstrip())
bomb = str(input().rstrip())

length = len(bomb)
stack = []

for i in target:
    stack.append(i)
    if i == bomb[-1]:
        if len(stack) >= length:
            if ''.join(stack[-length:]) == bomb:
                for _ in range(length):
                    stack.pop()

if not stack:
    print("FRULA")
else:
    print(''.join(stack))
