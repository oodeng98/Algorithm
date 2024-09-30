import sys


input = sys.stdin.readline

V = int(input())

tree = {i: {} for i in range(V+1)}
for i in range(V):
    temp = list(map(int, input().split()))
    start = temp[0]
    if start not in tree:
        tree[start] = {}
    for index, i in enumerate(temp):
        if index == 0:
            continue
        if i == -1:
            break
        tree[start]
        