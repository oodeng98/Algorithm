def dfs(data, start_num):
    stack = [start_num]
    via = [start_num]
    j = 0
    while True:
        if len(data) == 0 or j < -1000:
            break
        start_point = stack[j]  # 수정해줘야함
        remove_ele = 0
        append_ele = 1001
        for i in data:
            if i[0] == start_point and append_ele > i[1]:
                append_ele = i[1]
                remove_ele = i
            elif i[1] == start_point and append_ele > i[0]:
                append_ele = i[0]
                remove_ele = i
        if remove_ele != 0:
            data.remove(remove_ele)
        if append_ele not in via and append_ele != 1001:
            stack.append(append_ele)
            via.append(append_ele)
            j = len(stack) - 1
        else:
            j -= 1
            stack.pop(-1)
    return via


def bfs(data, start_num):
    queue = {start_num: 0}
    j = 0
    while True:
        if len(data) == 0 or j < -1000:
            break
        start_point = list(queue.keys())[j]
        remove_list = []
        append_list = []
        for i in data:
            if i[0] == start_point:
                append_list.append(i[1])
                remove_list.append(i)
            elif i[1] == start_point:
                append_list.append(i[0])
                remove_list.append(i)
        for i in remove_list:
            data.remove(i)
        append_list.sort()
        for i in append_list:
            queue[i] = 0
        j += 1
    return list(queue.keys())

import sys
sys.setrecursionlimit(2000)

input = sys.stdin.readline
dot_num, line_num, start_num = map(int, input().split())
data1 = []
for i in range(line_num):
    data1.append(tuple(map(int, input().split())))
data2 = [x for x in data1]
for i in dfs(data1, start_num):
    print(i, end=' ')
print()
for i in bfs(data2, start_num):
    print(i, end= ' ')
