import sys

class Node:
    def __init__(self, num):
        self.left = None
        self.right = None
        self.left_cost = 0
        self.right_cost = 0
        self.total_cost = 0
        self.left_total = 0
        self.right_total = 0
        self.parents = []
        self.num = num


def postorder(node):
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    left_total = 0
    if node.left:
        left_total = node.left_cost + node.left.total_cost

    right_total = 0
    if node.right:
        right_total = node.right_cost + node.right.total_cost
    node.left_total = left_total
    node.right_total = right_total
    node.total_cost = max(left_total, right_total)


input = sys.stdin.readline
# 가장 긴 길이를 가지는 두 노드를 구하면 될 듯?
# 노드 2개는 무조건 제일 아래에 있는 노드를 선택하는게 맞다

# 각 노드에 최댓값이라는 값이 들어가 있으면?
# 밑에 하나만 있는 애들의 최대값은 당연히 좌우 합
# 밑에 두개가 있는 애들의 최대값은 손자들의 최댓값과 그 위 가중치를 더한 값들을 비교하는 것
# 죄측 가중치 + 그 자식들의 가중치 합과 우측 가중치 + 그 자식들과의 가중치 합 중 가장 큰 부분을 선택하면 된다

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

# 후위 순회로 돌면서 마주치는 노드들마다 최대 지름 만들면서 올라가면 될 것 같은데?
postorder(node[1])
max_diameter = 0
for i in node[1:]:
    max_diameter = max(i.left_total + i.right_total, max_diameter)
print(max_diameter)