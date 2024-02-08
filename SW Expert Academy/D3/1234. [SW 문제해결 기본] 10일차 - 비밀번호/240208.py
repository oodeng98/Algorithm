import sys

sys.stdin = open('input.txt')
for t in range(1, 11):
    stack = []
    N, str1 = input().split()
    for i in str1:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    print(f"#{t} {''.join(stack)}")