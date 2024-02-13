import sys

sys.stdin = open('input.txt')

def forth():
    stack = []
    for i in temp:
        if i.isdecimal():
            stack.append(int(i))
        else:
            if i == '.':
                break
            if len(stack) < 2:
                return 'error'
            a = stack.pop()
            b = stack.pop()
            if i == '+':
                stack.append(a + b)
            elif i == '-':
                stack.append(a - b)
            elif i == '*':
                stack.append(a * b)
            elif i == '/':
                stack.append(a // b)
    return stack.pop()


T = int(input())
for t in range(1, T+1):
    temp = input().split()
    print(f"#{t} {forth()}")