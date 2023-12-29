import sys


def find_left(lst, idx):
    if lst[idx - 1] not in sign:
        return idx - 1
    count = 0
    for i in range(idx - 1, 0, -1):
        if ')' in lst[i]:
            count += 1
        elif '(' in lst[i]:
            count -= 1
            if count < 0:
                return i


def find_right(lst, idx):
    if lst[idx + 1] not in sign:
        return idx + 1
    count = 0
    for i in range(idx + 1, len(expression)):
        print(i)
        if '(' in lst[i]:
            count += 1
        elif ')' in lst[i]:
            count -= 1
            if count == 0:
                return i


input = sys.stdin.readline
expression = input().strip()
sign = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3, ')': 3}
stack = []
result = ''
for i in expression:
    if i in sign:
        if not stack:
            stack.append(i)
            continue
        if i == ')':
            while stack[-1] != '(':
                result += stack.pop()
            stack.pop()
            continue
        while stack and sign[stack[-1]] >= sign[i] and stack[-1] != '(':
            result += stack.pop()
        stack.append(i)
    else:
        result += i
while stack:
    result += stack.pop()
print(result)
