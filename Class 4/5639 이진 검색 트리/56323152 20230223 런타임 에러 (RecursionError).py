import sys


def family(lst):
    root = lst[0]
    cut = 1
    for index, node in enumerate(lst):
        if node > root:
            cut = index
            break
    left = lst[1:cut]
    right = lst[cut:]
    if left:
        family(left)
    if right:
        family(right)
    print(root)


input = sys.stdin.readline
data = []
while True:
    try:
        data.append(int(input()))
    except:
        break
family(data)
