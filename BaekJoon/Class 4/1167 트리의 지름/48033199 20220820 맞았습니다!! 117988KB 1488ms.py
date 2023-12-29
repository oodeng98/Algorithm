import sys
import heapq

class Node:
    def __init__(self, num):
        self.child = {}
        self.connect = {}  # node: cost
        self.two_cost = []
        self.max_cost = 0
        self.checked = 0
        self.num = num


def set_law(start_node):
    if start_node.checked:
        return
    start_node.checked = 1
    for ch in start_node.connect:
        if ch.checked == 0:
            start_node.child[ch] = start_node.connect[ch]
        set_law(ch)


def postorder(node):
    for ch in node.child:
        postorder(ch)
    if node.child:
        child_max = []
        for i in node.child:
            heapq.heappush(child_max, -(i.two_cost[0] + node.child[i]))
        i = 0
        while child_max and i < 2:
            node.two_cost.append(-heapq.heappop(child_max))
            i += 1
        node.max_cost = -sum(node.two_cost)
    else:
        node.two_cost = [0]


# sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n = int(input())
node = [0]
for i in range(n):
    node.append(Node(i + 1))
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(1, len(data) // 2):
        node[data[0]].connect[node[data[j * 2 - 1]]] = data[j * 2]

set_law(node[1])
postorder(node[1])
max_diameter = 0
for i in node[1:]:
    max_diameter = min(i.max_cost, max_diameter)
print(-max_diameter)