import sys


def binary_search(l, r, direction):
    if r < l:
        return False
    m = (l + r) // 2
    if target == lst1[m]:
        return True
    if lst1[m] < target:
        if direction == 'right':
            return False
        return binary_search(m+1, r, 'right')
    if direction == 'left':
        return False
    return binary_search(l, m-1, 'left')


sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    lst1 = list(map(int, input().split()))
    lst1.sort()
    lst2 = list(map(int, input().split()))
    result = 0
    for target in lst2:
        if binary_search(0, N-1, None):
            result += 1
    print(f"#{t} {result}")