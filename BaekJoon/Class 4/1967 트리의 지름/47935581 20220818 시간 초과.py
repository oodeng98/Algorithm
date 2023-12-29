import sys

class Node:
    def __init__(self, num):
        self.left = None
        self.right = None
        self.left_cost = None
        self.right_cost = None
        self.parents = []
        self.num = num

input = sys.stdin.readline
# 어떤 두 노드를 선택해도 둘 사이에 경로가 항상 하나만 존재
# 가장 긴 길이를 가지는 두 노드를 구하면 될 듯?
# 노드 2개는 무조건 제일 아래에 있는 노드를 선택하는게 맞다

n = int(input())
node = [0]
for i in range(n):
    node.append(Node(i + 1))
for i in range(n - 1):
    a, b, c = map(int, input().split())
    node[b].parents = node[a].parents + [a]
    if not node[a].left:
        node[a].left = node[b]
        node[a].left_cost = c
    else:
        node[a].right = node[b]
        node[a].right_cost = c

end = []
for nd in node[1:]:
    if not nd.left and not nd.right:
        end.append(nd.num)

max_diameter = 0
for i in range(len(end)):
    for j in range(i + 1, len(end)):
        parents1 = node[end[i]].parents
        parents2 = node[end[j]].parents
        target = 1
        for p in parents1:
            if p not in parents2:
                break
            target = p
        diameter = 0
        position = target
        while True:
            if node[position].left:
                diameter += node[position].left_cost
            else:
                break
            position = node[position].left.num

        position = target
        while True:
            if node[position].right:
                diameter += node[position].right_cost
            else:
                break
            position = node[position].right.num
        if diameter > max_diameter:
            max_diameter = diameter
print(max_diameter)
