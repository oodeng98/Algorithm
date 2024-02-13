import sys

sys.stdin = open('input.txt')

T = int(input())
stack = []
print(f"#{T}", end=' ')
for i in input():
    if i.isdecimal():
        print(i, end='')
    else:
        stack.append(i)
print(''.join(stack[::-1]), end='')