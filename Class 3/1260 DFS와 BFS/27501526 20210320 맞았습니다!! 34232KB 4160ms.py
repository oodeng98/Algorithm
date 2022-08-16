import sys
import copy
import collections


def dfs(data, start):
    stack = [start]
    result = [start]
    result_dic = {start: 0}
    while stack:
        process = stack[-1]
        temp = []
        for i in range(len(data)):
            if process in data[i]:
                if data[i][0] == process:
                    temp.append((data[i][1], i))
                else:
                    temp.append((data[i][0], i))
        if temp:
            append_process, sequence = min(temp, key=lambda x: x[0])
            if append_process not in result_dic:
                result.append(append_process)
                result_dic[append_process] = 0
                stack.append(append_process)
            data[sequence], data[-1] = data[-1], data[sequence]
            data.pop()
        else:
            stack.pop()
    return result


def bfs(data, start):
    queue = collections.deque([start])
    result = [start]
    result_dic = {start: 0}
    while queue:
        process = queue.popleft()
        temp = []
        for i in range(len(data)):
            if process in data[i]:
                if data[i][0] == process:
                    temp.append((data[i][1], i))
                else:
                    temp.append((data[i][0], i))
        if temp:
            temp.sort(key=lambda x: x[0])
            for i in temp:
                append_process, sequence = i
                queue.append(append_process)
                if append_process not in result_dic:
                    result_dic[append_process] = 0
                    result.append(append_process)
            temp.sort(key=lambda x: x[1], reverse=True)
            for i in temp:
                append_process, sequence = i
                data[sequence], data[-1] = data[-1], data[sequence]
                data.pop()
    return result


input = sys.stdin.readline
dot_num, line_num, start_num = map(int, input().split())
data1 = []
for j in range(line_num):
    data1.append(tuple(map(int, input().split())))
data2 = copy.deepcopy(data1)
print(' '.join(map(str, dfs(data1, start_num))))
print(' '.join(map(str, bfs(data2, start_num))))


"""
동주가 말해준 방법으로 짤 수 있을 것 같다. 하지만 이 코드가 왜 틀렸는지는 아직도 모르겠다.
"""
'''
graph = [[] for n in range(dot_num + 1)]
for i in range(line_num):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for n in range(dot_num + 1):
    graph[n].sort()
visited = [False] * (dot_num + 1)


def bfs(root):
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if not visited[node]:
            visited[node] = True
            queue.extend(graph[node])
'''


"""
def dfs(root):
    stack = []
    while stack:
        node = stack.pop()
        for child in graph[node]:
            if not visited[child]:
                stack.append(child)
        if not visited[node]:
            stack.append()
            # homeless가 되어야 visited=True
"""