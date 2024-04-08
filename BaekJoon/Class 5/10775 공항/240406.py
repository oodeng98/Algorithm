import sys


input = sys.stdin.readline
G = int(input())
P = int(input())
airport = [-1 for _ in range(G+1)]
planes = [int(input()) for _ in range(P)]
result = 0
for plane in planes:
    p = plane
    while airport[p] != -1:
        p = airport[p]  # 저장되지 않은 위치로 이동
    if p == 0:
        break
    result += 1
    airport[p] = p - 1  # 왼쪽 지정
    airport[plane] = p - 1
print(result)