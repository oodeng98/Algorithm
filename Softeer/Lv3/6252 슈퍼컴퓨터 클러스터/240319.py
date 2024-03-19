import sys
import math


def cost(l):
    ret = 0
    for i in computers:
        if i < l:
            ret += (l - i) ** 2
    return ret

N, B = map(int, input().split())
computers = list(map(int, input().split()))
start = 0
end = max(computers) + int(math.sqrt(B // (N-1)))
while True:
    if end < start:
        break
    middle = (start + end) // 2
    temp = cost(middle)
    if temp < B:
        start = middle + 1
    elif B < temp:
        end = middle - 1
    else:
        break
if B < cost(middle):
    print(middle - 1)
else:
    print(middle)