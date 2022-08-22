import sys
from heapq import heappop, heappush


def make_tree(root_node, left_index, right_index):
    print(root_node, end=' ')
    target_index = inorder_dict[root_node]
    if target_index - left_index > 1:
        heap = []
        for i in range(left_index, target_index):
            heappush(heap, (-postorder_dict[inorder[i]], inorder[i]))
        make_tree(heappop(heap)[1], left_index, target_index)
    elif target_index - left_index == 1:
        print(inorder[left_index], end=' ')

    if right_index - target_index - 1 > 1:
        heap = []
        for i in range(target_index + 1, right_index):
            heappush(heap, (-postorder_dict[inorder[i]], inorder[i]))
        make_tree(heappop(heap)[1], target_index + 1, right_index)
    elif right_index - target_index - 1 == 1:
        print(inorder[target_index + 1], end=' ')


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
for index, i in enumerate(postorder):
    postorder_dict[i] = index

make_tree(postorder[-1], 0, len(inorder))
