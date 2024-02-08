import sys

sys.stdin = open('input.txt')
for t in range(1, int(input()) + 1):
    stack = []
    for i in input():
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    print(f"#{t} {len(stack)}")