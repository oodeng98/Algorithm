import sys

sys.setrecursionlimit(1000000)

def dfs(node):
    visited[node] = 1
    
    temp = [0]
    for i in tree[node]:
        if visited[i]:
            continue
        temp.append(dfs(i) + tree[node][i])
        
    temp.sort(reverse=True)
    if 2 <= len(temp):
        result[0] = max(result[0], temp[0] + temp[1])
    else:
        result[0] = max(result[0], temp[0])
    return temp[0]


input = sys.stdin.readline

V = int(input())
tree = {i: {} for i in range(1, V+1)}
for _ in range(V):
    temp = list(map(int, input().split()))
    start = temp[0]
    for index, i in enumerate(temp):
        if index % 2 == 0:
            continue
        if i == -1:
            break
        tree[start][i] = temp[index+1]
        tree[i][start] = temp[index+1]

visited = [0 for _ in range(V+1)]
result = [0]
dfs(1)
# print(visited)
print(result[0])
