import sys


def push_front(deque, ele):
    deque.insert(0, ele)


def push_back(deque, ele):
    deque.append(ele)


def pop_front(deque):
    if len(deque) == 0:
        print(-1)
    else:
        print(deque.pop(0))


def pop_back(deque):
    if len(deque) == 0:
        print(-1)
    else:
        print(deque.pop(-1))


def size(deque):
    print(len(deque))


def empty(deque):
    if len(deque) == 0:
        print(1)
    else:
        print(0)


def front(deque):
    if len(deque) == 0:
        print(-1)
    else:
        print(deque[0])


def back(deque):
    if len(deque) == 0:
        print(-1)
    else:
        print(deque[-1])


input = sys.stdin.readline

num = int(input())
order = []
for i in range(num):
    order.append(input().split())

deq = []
for i in order:
    if i[0] == 'push_front':
        push_front(deq, i[1])
    elif i[0] == 'push_back':
        push_back(deq, i[1])
    elif i[0] == 'pop_front':
        pop_front(deq)
    elif i[0] == 'pop_back':
        pop_back(deq)
    elif i[0] == 'size':
        size(deq)
    elif i[0] == 'empty':
        empty(deq)
    elif i[0] == 'front':
        front(deq)
    elif i[0] == 'back':
        back(deq)