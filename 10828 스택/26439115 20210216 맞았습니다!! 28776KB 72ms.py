import sys


def push(stack, ele):
    stack.append(ele)


def pops(stack):
    if len(stack) == 0:
        print(-1)
    else:
        print(stack.pop(-1))


def size(stack):
    print(len(stack))


def empty(stack):
    if len(stack) == 0:
        print(1)
    else:
        print(0)


def top(stack):
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])


input = sys.stdin.readline

num = int(input())
stack = []
for i in range(num):
    temp = input().split()
    if temp[0] == 'push':
        push(stack, temp[1])
    elif temp[0] == 'pop':
        pops(stack)
    elif temp[0] == 'size':
        size(stack)
    elif temp[0] == 'empty':
        empty(stack)
    elif temp[0] == 'top':
        top(stack)