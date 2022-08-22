import sys
from heapq import heappop, heappush


def make_tree(in_left, in_right, post_left, post_right):
    if in_left > in_right or post_left > post_right:
        return
    root = postorder[post_right]
    print(root, end=' ')
    index = inorder_dict[root]
    count = index - in_left
    make_tree(in_left, index - 1, post_left, post_left + count - 1)
    make_tree(index + 1, in_right, post_left + count, post_right - 1)

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
inorder_dict = {}
for index, i in enumerate(inorder):
    inorder_dict[i] = index
postorder_dict = {}

make_tree(0, len(inorder) - 1, 0, len(inorder) - 1)

