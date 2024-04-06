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

'''
내 번호에 자리가 있다면 일단 그 자리로 가는 것이 이득
내 번호에 자리가 없으면 남은 자리 중 가장 큰 자리로 이동
이 로직을 어떻게 구현하느냐
4
4
3
1
이러면 가능
4
4
4
3
이건 가능인데
큰 수는 언제든 작은 수로 바뀔 수 있는데
작은 수는 큰 수로 바뀔 수가 없어요
내 앞에 나보다 작은 비행기가 몇개나 있느냐..가 문제
비행기 번호만큼의 비행기가 있으면 그냥 포기하면 됨
다 heapq에 때려박으면 (비행기 번호, 순서)로 들어갈거고..
비행기 번호가 작은 애들이 먼저 나올테니
근데 이미 그 앞에서 
4
4
4
4
1
이런식으로 나왔으면 연산 더 해줘야함
젠 장
'''