import sys

sys.stdin = open('input.txt')
for t in range(1, int(input())+1):
    v, e = map(int, input().split())
    graph = {i: [] for i in range(1, v+1)}
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
    start, end = map(int, input().split())
    stack = [start]
    visit = [0 for _ in range(v+1)]
    check = 0
    while stack:
        now = stack.pop()
        if visit[now] == 1:
            continue
        for i in graph[now]:
            if visit[i] == 0:
                if i == visit:
                    check = 1
                    break
                stack.append(i)
        if check:
            break
    if check:
        print(f"#{t} 0")
    else:
        print(f"#{t} 1")