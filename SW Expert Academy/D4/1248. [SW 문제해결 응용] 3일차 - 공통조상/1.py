T = int(input())

for t in range(T):
    V, E, a, b = map(int, input().split())
    edges = list(map(int, input().split()))
    tree = {}
    parent = {}
    for i in range(0, E * 2, 2):
        x, y = edges[i], edges[i+1]
        parent[y] = x
        if edges[i] not in tree:
            tree[x] = [y]
        else:
            tree[x].append(y)

    height = [0 for _ in range(V + 1)]

    # 노드 높이 설정
    h = 1
    height[1] = h
    children = tree[1]
    while True:
        h += 1
        new_children = []
        for child in children:
            height[child] = h
            if child in tree:
                new_children.extend(tree[child])
        children = new_children
        if not children:
            break

    # 노드의 높이 맞춰주기
    nodeA = a
    nodeB = b
    while height[nodeA] != height[nodeB]:
        if height[nodeA] > height[nodeB]:
            nodeA = parent[nodeA]
        else:
            nodeB = parent[nodeB]

    while nodeA != nodeB:
        nodeA = parent[nodeA]
        nodeB = parent[nodeB]
    
    children = tree[nodeA]
    count = len(children) + 1
    while True:
        new_children = []
        for child in children:
            if child in tree:
                new_children.extend(tree[child])
        children = new_children
        count += len(children)
        if not children:
            break

    print(f"#{t+1} {nodeA} {count}")

"""
1
13 12 8 13
1 2 1 3 2 4 3 5 3 6 4 7 7 12 5 9 5 8 6 11 6 10 11 13
"""