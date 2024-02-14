import sys

sys.stdin = open('input.txt')


def win(a, b):
    if a == b:
        return 1
    if a == '1':
        if b == '2':
            return 0
        else:
            return 1
    elif a == '2':
        if b == '3':
            return 0
        else:
            return 1
    else:
        if b == '1':
            return 0
        else:
            return 1


def divide(start, end):
    if end - start <= 1:
        if win(lst[start], lst[end]) == 1:
            return start
        return end
    a = divide(start, (start+end)//2)
    b = divide((start+end)//2+1, end)
    if win(lst[a], lst[b]) == 1:
        return a
    return b
    

T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = input().split()
    # 1: 가위, 2: 바위, 3: 보
    print(f"#{t} {divide(0, N-1)+1}")