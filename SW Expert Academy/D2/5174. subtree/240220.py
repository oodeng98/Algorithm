import sys

sys.stdin = open('input.txt')

def preorder(node):
    if node not in graph:
        return 1
    total = 0
    for i in graph[node]:
        total += preorder(i)
    return total + 1

T = int(input())
for t in range(1, T+1):
    e, n = input().split()
    graph = {}
    temp = input().split()
    for i in range(int(e)):
        a, b = temp[2*i], temp[2*i+1]
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]
    print(f"#{t} {preorder(n)}")