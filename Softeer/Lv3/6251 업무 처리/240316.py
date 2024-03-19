import sys
from collections import deque
import math

input = sys.stdin.readline
H, K, R = map(int, input().split())
tree = [deque([]) for _ in range(2 ** (H + 1))]
for i in range(2 ** H):
    tree[2**H+i].extend(list((map(int, input().split()))))
# 말단 노드의 레벨은 H
# H-홀수번째 레벨의 노드는 오른쪽부터 처리
# H-짝수번째 레벨의 노드는 왼쪽부터 처리
result = 0
for r in range(R):
    if tree[1]:
        result += tree[1].popleft()
    for i in range(1, 2 ** H):
        level = int(math.log2(i))
        if tree[i*2]:
            if level % 2 != H % 2:
                tree[i].append(tree[i*2+1].popleft())
                tree[i].append(tree[i*2].popleft())
            else:
                tree[i].append(tree[i*2].popleft())
                tree[i].append(tree[i*2+1].popleft())
print(result)