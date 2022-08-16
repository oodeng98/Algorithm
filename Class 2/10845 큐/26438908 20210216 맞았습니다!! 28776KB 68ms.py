import sys


def push(queue, ele):
    queue.append(ele)


def pops(queue):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue.pop(0))


def size(queue):
    print(len(queue))


def empty(queue):
    if len(queue) == 0:
        print(1)
    else:
        print(0)


def front(queue):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])


def back(queue):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[-1])


input = sys.stdin.readline

num = int(input())
queue = []
for i in range(num):
    temp = input().split()
    if temp[0] == 'push':
        push(queue, temp[1])
    elif temp[0] == 'pop':
        pops(queue)
    elif temp[0] == 'size':
        size(queue)
    elif temp[0] == 'empty':
        empty(queue)
    elif temp[0] == 'front':
        front(queue)
    elif temp[0] == 'back':
        back(queue)