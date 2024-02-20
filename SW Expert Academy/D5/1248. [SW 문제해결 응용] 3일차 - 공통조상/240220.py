import sys

sys.stdin = open('input.txt')


def node_height(node_num):
    node = node_num
    count = 0
    while node != 1:
        node = parent[node]
        count += 1
    return count


def union_find(node_a, node_b):
    rank_a = node_height(node_a)
    rank_b = node_height(node_b)

    if rank_b < rank_a:
        rank_a, rank_b = rank_b, rank_a
        node_a, node_b = node_b, node_a
    
    while rank_a != rank_b:
        node_b = parent[node_b]
        rank_b -= 1
    
    while node_a != node_b:
        node_a = parent[node_a]
        node_b = parent[node_b]
    return node_a


def preorder(node):
    if node not in graph:
        return 1
    total = 0
    for i in graph[node]:
        total += preorder(i)
    return total + 1


T = int(input())
for t in range(1, T+1):
    v, e, node_a, node_b = map(int, input().split())
    parent = [0 for i in range(v+1)]
    graph = {}
    temp = list(map(int, input().split()))
    for i in range(e):
        a, b = temp[2*i], temp[2*i+1]
        parent[b] = a
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]
    
    result = union_find(node_a, node_b)
    print(f"#{t} {result} {preorder(result)}")