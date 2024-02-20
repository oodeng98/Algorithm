import sys

sys.stdin = open('input.txt')


def preorder(node):
    print(node, end=' ')
    if node not in graph:
        return
    for i in graph[node]:
        preorder(i)


V = int(input())
graph = {}
temp = input().split()
for i in range(V-1):
    a, b = temp[2*i], temp[2*i+1]
    if a in graph:
        if b < graph[a][0]:
            graph[a].insert(0, b)
        else:
            graph[a].append(b)
    else:
        graph[a] = [b]
preorder('1')