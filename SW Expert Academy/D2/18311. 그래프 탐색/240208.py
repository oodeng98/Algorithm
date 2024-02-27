import sys

def countSort(arr):
    length = len(arr)
    temp_lst = [0 for _ in range(v+1)]
    result_lst = [0 for _ in range(length)]
    for i in arr:
        temp_lst[i] += 1
    for i in range(v, 1, -1):
        temp_lst[i-1] += temp_lst[i]
    for i in range(length-1, -1, -1):
        a = arr[i]
        temp_lst[a] -= 1
        result_lst[temp_lst[a]] = a
    return result_lst

sys.stdin = open('input.txt')
v, e = map(int, input().split())
graph = {}
temp = list(map(int, input().split()))
for i in range(e):
    a, b = temp[i*2], temp[i*2+1]
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]
    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]

stack = [1]
visit = [0] * (v + 1)
result = []
while stack:
    now = stack.pop()
    if visit[now]:
        continue
    visit[now] = 1
    result.append(now)
    graph[now] = countSort(graph[now])
    for i in graph[now]:
        if visit[i] == 1:
            continue
        stack.append(i)
print(f"#1 {'-'.join(map(str, result))}")
