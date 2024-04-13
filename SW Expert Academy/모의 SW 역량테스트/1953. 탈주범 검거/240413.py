import sys

sys.stdin = open('input.txt')


from collections import deque


tunnel = {
    '0': {}, 
    '1': {'u', 'd', 'r', 'l'}, 
    '2': {'u', 'd'}, 
    '3': {'r', 'l'}, 
    '4': {'u', 'r'}, 
    '5': {'d', 'r'}, 
    '6': {'d', 'l'}, 
    '7': {'u', 'l'}, 
}
    

def bfs():
    queue = {(R, C)}
    visit = [[0 for _ in range(M)] for _ in range(N)]
    visit[R][C] = 1
    result = 0
    for i in range(L-1):
        result += len(queue)
        new_queue = set()
        for j in queue:
            x, y = j
            if 'u' in tunnel[arr[x][y]]:
                a, b = x - 1, y
                if 0 <= a < N and 0 <= b < M and 'd' in tunnel[arr[a][b]] and visit[a][b] == 0:
                    new_queue.add((a, b))
                    visit[a][b] = 1
            if 'd' in tunnel[arr[x][y]]:
                a, b = x + 1, y
                if 0 <= a < N and 0 <= b < M and 'u' in tunnel[arr[a][b]] and visit[a][b] == 0:
                    new_queue.add((a, b))
                    visit[a][b] = 1
            if 'r' in tunnel[arr[x][y]]:
                a, b = x, y + 1
                if 0 <= a < N and 0 <= b < M and 'l' in tunnel[arr[a][b]] and visit[a][b] == 0:
                    new_queue.add((a, b))
                    visit[a][b] = 1
            if 'l' in tunnel[arr[x][y]]:
                a, b = x, y - 1
                if 0 <= a < N and 0 <= b < M and 'r' in tunnel[arr[a][b]] and visit[a][b] == 0:
                    new_queue.add((a, b))
                    visit[a][b] = 1
        queue = new_queue
    result += len(queue)
    return result


T = int(input())
for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [input().split() for _ in range(N)]
    print(f"#{t} {bfs()}")