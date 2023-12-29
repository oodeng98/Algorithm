import sys

input = sys.stdin.readline
target = list(input().rstrip())
target.reverse()
stack = []
bomb = input().rstrip()
index = 0
while len(bomb) <= len(target):  # bomb의 길이가 1인 경우는?!
    temp1 = target[-1]
    if temp1 == bomb[0]:
        check = 1
        for i in range(1, len(bomb) + 1):
            temp2 = target[-i]
            if temp2 != bomb[i - 1]:
                check = 0
                break
        if check:
            for i in range(len(bomb)):
                target.pop()
            for i in range(len(bomb)):
                if stack:
                    target.append(stack.pop())
                else:
                    break
    stack.append(target.pop())
target.reverse()
stack.extend(target)
if not stack or ''.join(stack) == bomb:
    print("FRULA")
else:
    print(''.join(stack))
