import sys


def quick_sort(lst, l, r):
    if l < r:
        s = partition(lst, l, r)
        quick_sort(lst, l, s-1)
        quick_sort(lst, s+1, r)


def partition(lst, l, r):
    p = lst[l]
    i, j = l, r
    while i <= j:
        while i <= j and lst[i] <= p:
            i += 1
        while i <= j and p <= lst[j]:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    lst[l], lst[j] = lst[j], lst[l]
    return j




sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T+1):
    lst = list(map(int, input().split()))
    quick_sort(lst, 0, len(lst)-1)
    print(f"#{t} {' '.join(map(str, lst))}")