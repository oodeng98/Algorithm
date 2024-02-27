import sys

sys.stdin = open('input.txt')


def tree(node):
    global num
    if node <= N:
        tree(2 * node)
        arr[node] = num
        num += 1
        tree(2 * node + 1)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [0 for _ in range(N+1)]
    num = 1
    tree(1)
    print(f"#{t} {arr[1]} {arr[N//2]}")