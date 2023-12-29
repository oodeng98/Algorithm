import sys


class Node:
    def __init__(self, num):
        self.left = None
        self.right = None
        self.num = num


def make_tree(root_node, left_index, right_index):
    if len(inorder) <= 1:
        return
    target_index = inorder.index(root_node.num)
    if target_index - left_index > 1:
        max_index = 0
        left_node = -1
        for i in range(left_index, target_index):
            if postorder_dict[inorder[i]] >= max_index:
                max_index = postorder_dict[inorder[i]]
                left_node = inorder[i]
        root_node.left = Node(left_node)
        make_tree(root_node.left, left_index, target_index)
    elif target_index - left_index == 1:
        root_node.left = Node(inorder[left_index])

    if right_index - target_index - 1 > 1:
        max_index = 0
        right_node = -1
        for i in range(target_index + 1, right_index):
            if postorder_dict[inorder[i]] >= max_index:
                max_index = postorder_dict[inorder[i]]
                right_node = inorder[i]
        root_node.right = Node(right_node)
        make_tree(root_node.right, target_index + 1, right_index)
    elif right_index - target_index - 1 == 1:
        root_node.right = Node(inorder[target_index + 1])


def preorder(node):
    lst.append(node.num)
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)


sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n = int(input())
inorder = list(map(int, input().split()))  # 중위 순회
postorder = list(map(int, input().split()))  # 후위 순회
# 전위 순회를 구하라
'''
중위 순회 7->3->8->1->9->4->10->0->11->5->2->6
후위 순회 7->8->3->9->10->4->1->11->5->6->2->0 => 0이 루트 노드라는 것을 알 수 있음
중위 순회에서 7->3->8->1->9->4->10 이건 왼쪽 트리
이중 후위 순회에서 가장 늦게 나오는 1이 또 루트 노드
11
7 3 8 1 9 4 10 0 11 5 2 6
7 8 3 9 10 4 1 11 5 6 2 0
답:
0 1 3 7 8 4 9 10 2 5 11 6
'''
postorder_dict = {}
for index, i in enumerate(postorder):
    postorder_dict[i] = index

root_node = Node(postorder[-1])
make_tree(root_node, 0, len(inorder))
lst = []
preorder(root_node)
for i in lst[:-1]:
    print(i, end=' ')
print(lst[-1])
