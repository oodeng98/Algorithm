import sys

sys.stdin = open('input.txt')


def inorder(nodeNum):
    if tree[nodeNum][0] == '+':
        return inorder(tree[nodeNum][1]) + inorder(tree[nodeNum][2])
    if tree[nodeNum][0] == '-':
        return inorder(tree[nodeNum][1]) - inorder(tree[nodeNum][2])
    if tree[nodeNum][0] == '/':
        return inorder(tree[nodeNum][1]) / inorder(tree[nodeNum][2])
    if tree[nodeNum][0] == '*':
        return inorder(tree[nodeNum][1]) * inorder(tree[nodeNum][2])
    return tree[nodeNum][0]


for t in range(1, 11):
    N = int(input())
    tree = {}
    for _ in range(N):
        a, b, *c = input().split()
        if c:
            tree[int(a)] = [b] + list(map(int, c))
        else:
            tree[int(a)] = [int(b)]
    print(f"#{t} {int(inorder(1))}")