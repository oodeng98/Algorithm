import sys

sys.stdin = open('input.txt')
while True:
    try:
        t, length = map(int, input().split())
    except:
        break
    graph = {i: [] for i in range(100)}
    road = list(map(int, input().split()))
    for i in range(length):
        a, b = road[i*2], road[i*2+1]
        graph[a].append(b)

    des = 99
    stack = [0]
    visit = [0 for _ in range(100)]
    check = 0
    while stack:
        now = stack.pop()
        for i in graph[now]:
            if visit[i] == 1:
                continue
            if i == des:
                check = 1
                break
            stack.append(i)
        if check:
            break
    if check:
        print(f"#{t} 1")
        continue
    print(f"#{t} 0")

