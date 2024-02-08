import sys

sys.stdin = open('input.txt')
for t in range(1, int(input().strip()) + 1):
    stack = []
    check = 1
    for i in input().strip():
        if i == '(':
            stack.append(i)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                check = 0
                break
    if stack or check == 0:
        print(f"#{t} -1")
    else:
        print(f"#{t} 1")
    