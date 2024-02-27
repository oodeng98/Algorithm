import sys

sys.stdin = open('input.txt')


def win(a, b):
    if lst[a] == lst[b]:
        return a
    if lst[a] == '1':
        if lst[b] == '2':
            return b
        return a
    elif lst[a] == '2':
        if lst[b] == '3':
            return b
        return a
    else:
        if lst[b] == '1':
            return b
        return a


def divide(start, end):
    if end - start <= 1:
        return win(start, end)
    return win(divide(start, (start+end)//2), divide((start+end)//2+1, end))


T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = input().split()
    # 1: 가위, 2: 바위, 3: 보
    print(f"#{t} {divide(0, N-1)+1}")