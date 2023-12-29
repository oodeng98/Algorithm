import sys
import copy
import collections


def dfs(data, start):
    stack = [(0, start)]
    result = {start: 0}
    while data:
        process = stack[-1]
        temp = []
        for i in range(len(data)):
            if process[1] in data[i]:
                if data[i][0] == process[1]:
                    temp.append((data[i], i))
                else:
                    temp.append(((data[i][1], data[i][0]), i))
        if temp:
            process, sequence = min(temp, key=lambda x: x[0][1])
            stack.append(process)
            data[sequence], data[-1] = data[-1], data[sequence]
            data.pop()
            if process[1] not in result:
                result[process[1]] = 0
        else:
            stack.pop()
    return result


def bfs(data, start):
    queue = collections.deque([(0, start)])
    result = {start: 0}
    while True:
        process = queue.popleft()
        temp = []
        for i in range(len(data)):
            if process[1] in data[i]:
                if data[i][0] == process[1]:
                    temp.append((data[i], i))
                else:
                    temp.append(((data[i][1], data[i][0]), i))
        if temp:
            temp.sort(key=lambda x: x[0][1])
            for i in temp:
                process, sequence = i
                queue.append(process)
                data[sequence] = (0, 0)
                if process[1] not in result:
                    result[process[1]] = 0
        else:
            break
    return result


input = sys.stdin.readline
dot_num, line_num, start_num = map(int, input().split())
data1 = []
for i in range(line_num):
    data1.append(tuple(map(int, input().split())))
data2 = copy.deepcopy(data1)
for i in dfs(data1, start_num):
    print(i, end=' ')
print()
for i in bfs(data2, start_num):
    print(i, end=' ')
