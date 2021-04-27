import sys


def preorder(tree, now):
    if now == '.' or now == 0:
        return
    print(now, end='')
    preorder(tree, tree[now][0])
    preorder(tree, tree[now][1])


def inorder(tree, now):
    if now == '.' or now == 0:
        return
    inorder(tree, tree[now][0])
    print(now, end='')
    inorder(tree, tree[now][1])


def postorder(tree, now):
    if now == '.' or now == 0:
        return
    postorder(tree, tree[now][0])
    postorder(tree, tree[now][1])
    print(now, end='')


input = sys.stdin.readline
n = int(input())
data = {}
for i in range(n):
    a, b, c = input().split()
    data[a] = [b, c]
preorder(data, "A")
print()
inorder(data, "A")
print()
postorder(data, "A")
