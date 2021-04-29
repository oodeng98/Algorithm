import sys


def postorder(trees, now):
    if now == -1:
        return
    postorder(trees, trees[now][0])
    postorder(trees, trees[now][1])
    print(now)


input = sys.stdin.readline
data = []
while True:
    try:
        data.append(int(input()))
    except:
        break
index = 2
tree = {data[0]: [-1, -1]}
if data[0] < data[1]:
    tree[data[0]][1] = data[1]
else:
    tree[data[0]][0] = data[1]
tree[data[1]] = [-1, -1]

for index in range(2, len(data)):
    start = data[0]
    while True:  # 자신과 자신의 부모 노드 사이에 있으면 오른쪽에 추가, 그게 아니면 왼쪽에 추가
        if start < data[index]:
            new_start = tree[start][1]
        else:  # data[index] < start
            new_start = tree[start][0]
        if new_start == -1:
            if start < data[index]:
                tree[start][1] = data[index]
            else:
                tree[start][0] = data[index]
            tree[data[index]] = [-1, -1]
            break
        start = new_start
postorder(tree, data[0])
