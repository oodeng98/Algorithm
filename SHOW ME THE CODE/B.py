import sys


def find_near(pos):
    post = [((pos[0] + 1) % N, pos[1]), ((pos[0] - 1 + N) % N, pos[1]), (pos[0], (pos[1] + 1) % M),
            (pos[0], (pos[1] - 1 + M) % M)]
    return post


input = sys.stdin.readline
N, M = map(int, input().split())
area = []
for i in range(N):
    area.append(list(map(int, input().split())))

count = 0
for i in range(N):
    for j in range(M):
        if area[i][j] == 0:
            candidate = {(i, j)}
            while True:
                next_candidate = set()
                for k in candidate:
                    for l in find_near(k):
                        if not area[l[0]][l[1]]:
                            area[l[0]][l[1]] = 1
                            next_candidate.add((l[0], l[1]))
                if not next_candidate:
                    break
                candidate = next_candidate
            count += 1

print(count)
