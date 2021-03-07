import sys

input = sys.stdin.readline

stack = []
result = []
while True:
    temp = input()
    if temp == '.\n':
        break
    check = 0
    for i in temp:
        if i == '(':
            stack.append('(')
        elif i == '[':
            stack.append('[')
        elif i == ')':
            if len(stack) == 0:
                result.append('no')
                check = 1
                break
            else:
                if stack.pop(-1) != '(':
                    result.append('no')
                    check = 1
                    break
        elif i == ']':
            if len(stack) == 0:
                result.append('no')
                check = 1
                break
            else:
                if stack.pop(-1) != '[':
                    result.append('no')
                    check = 1
                    break
    if check == 0 and len(stack) == 0:
        result.append('yes')
    else:
        result.append('no')

for i in result:
    print(i)