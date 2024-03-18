import sys


def quick_sort(l, r):
    if l < r:
        p = partition(l, r)
        quick_sort(l, p-1)
        quick_sort(p+1, r)


def partition(l, r):
    pivot = l
    i, j = l, r
    while i <= j:
        while i <= j and lst[i] <= lst[pivot]:
            i += 1
        while i <= j and lst[pivot] < lst[j]:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    lst[pivot], lst[j] = lst[j], lst[pivot]
    return j


sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    quick_sort(0, N-1)
    print(f"#{t} {lst[N//2]}")