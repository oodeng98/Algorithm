import sys
import heapq

class Node:
    def __init__(self, num):
        self.child = {}  # node: cost
        self.two_cost = []
        self.max_cost = 0
        self.num = num


def postorder(node):
    for ch in node.child:
        postorder(ch)
    if node.child:
        child_max = []
        for i in node.child:
            heapq.heappush(child_max, -(max(i.two_cost) + node.child[i]))
        i = 0
        while child_max and i < 2:
            node.two_cost.append(-heapq.heappop(child_max))
            i += 1
        node.max_cost = -sum(node.two_cost)
    else:
        node.two_cost = [0]


input = sys.stdin.readline
n = int(input())
node = [0]
for i in range(n):
    node.append(Node(i + 1))
for i in range(n - 1):
    a, b, c = map(int, input().split())
    node[a].child[node[b]] = c

postorder(node[1])
max_diameter = 0
for i in node[1:]:
    max_diameter = min(i.max_cost, max_diameter)
print(-max_diameter)
'''
5
1 2 3
1 3 4
1 4 5
1 5 6
반례
'''