import sys
sys.setrecursionlimit(10**5)


def family(start, end):
    if start + 1 >= end:
        print(data[start])
        return
    root = data[start]
    cut = end
    for index in range(start + 1, end):
        if data[index] > root:
            cut = index
            break
    family(start + 1, cut)
    family(cut, end)
    print(root)


input = sys.stdin.readline
data = []
while True:
    try:
        data.append(int(input()))
    except:
        break
family(0, len(data) - 1)
