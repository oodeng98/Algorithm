import sys

sys.stdin = open('input.txt')
for t in range(1, int(input()) + 1):
    N = int(input())
    print(f"#{t}")

    stack = [0, 1, 0]
    print(1)
    for i in range(1, N):
        next_stack = [0]
        for j in range(i+1):
            next_stack.append(stack[j] + stack[j+1])
        next_stack.append(0)
        print(' '.join(map(str, next_stack[1:-1])))
        stack = next_stack

