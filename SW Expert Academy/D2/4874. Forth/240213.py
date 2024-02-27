import sys

sys.stdin = open('input.txt')

def forth():
    stack = []
    for i in temp[:-1]:
        if i.isdecimal():
            stack.append(int(i))
        else:
            if len(stack) < 2:
                return 'error'
            b = stack.pop()
            a = stack.pop()
            if i == '+':
                stack.append(a + b)
            elif i == '-':
                stack.append(a - b)
            elif i == '*':
                stack.append(a * b)
            elif i == '/':
                stack.append(a // b)
    if len(stack) != 1:
        return 'error'
    return stack.pop()


T = int(input())
for t in range(1, T+1):
    temp = input().split()
    print(f"#{t} {forth()}")