import sys

sys.stdin = open('input.txt')


def findNum(nodeNum):
    if N < nodeNum:
        return 0
    if tree[nodeNum] != 0:
        return tree[nodeNum]
    return findNum(nodeNum*2) + findNum(nodeNum*2+1)


T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        tree[a] = b
    print(f"#{t} {findNum(L)}")