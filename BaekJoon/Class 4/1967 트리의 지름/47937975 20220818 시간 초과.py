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
dic = {}
for i in range(len(end)):
    dic[end[i]] = {}
    for j in range(i + 1, len(end)):
        if end[j] not in dic:
            dic[end[j]] = {}
        parents1 = node[end[i]].parents
        parents2 = node[end[j]].parents
        common = 1
        for p in parents1:
            if p not in parents2:
                break
            common = p

        if common not in dic[end[i]]:
            left_diameter = 0
            position = common
            while node[position].left:
                left_diameter += node[position].left_cost
                position = node[position].left.num
            dic[end[i]][common] = left_diameter
        else:
            left_diameter = dic[end[i]][common]

        if common not in dic[end[j]]:
            right_diameter = 0
            position = common
            while node[position].right:
                right_diameter += node[position].right_cost
                position = node[position].right.num
            dic[end[j]][common] = right_diameter
        else:
            right_diameter = dic[end[j]][common]

        if left_diameter + right_diameter > max_diameter:
            max_diameter = left_diameter + right_diameter
print(max_diameter)
