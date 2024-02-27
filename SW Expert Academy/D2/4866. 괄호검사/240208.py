import sys

sys.stdin = open("input.txt")
for t in range(1, int(input()) + 1):
    stack = []
    check = 0
    for i in input():
        if i in ['(', '{']:
            stack.append(i)
        elif i == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                check = 1
                break
        elif i == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                check = 1
                break
    if stack or check:
        print(f"#{t} 0")
    else:
        print(f"#{t} 1")