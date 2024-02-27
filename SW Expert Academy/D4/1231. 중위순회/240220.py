import sys

sys.stdin = open('input.txt')


def inorder(node_num):
    node = graph[node_num]
    if 1 <= len(node[1]):
        inorder(node[1][0])
    print(node[0], end='')
    if 2 <= len(node[1]):
        inorder(node[1][1])


for t in range(1, 11):
    n = int(input())
    graph = {}
    for _ in range(n):
        temp = input().split()
        a = temp[0]
        graph[a] = [temp[1], []]
        for i in temp[2:]:
            graph[a][1].append(i)
    print(f"#{t}", end=' ')
    inorder('1')
    print()
    