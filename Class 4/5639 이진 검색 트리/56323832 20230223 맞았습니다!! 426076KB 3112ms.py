import sys
sys.setrecursionlimit(10**5)


def family(lst):
    root = lst[0]
    cut = 1
    for index, node in enumerate(lst):
        if node > root:
            cut = index
            break
    left = lst[1:cut]
    right = lst[cut:]
    for child in [left, right]:
        length = len(child)
        if length == 1:
            print(child[0])
        elif length > 1:
            family(child)
    print(root)


input = sys.stdin.readline
data = []
while True:
    try:
        data.append(int(input()))
    except:
        break
family(data)
