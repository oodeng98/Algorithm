import sys

def range_check(a, b):
    result = []
    if 0 < a - 1:
        result.append((a - 1 , b))
    if a + 1 < n:
        result.append((a + 1 , b))
    if 0 < b - 1:
        result.append((a, b - 1))
    if b + 1 < m:
        result.append((a, b + 1))
    return result


input = sys.stdin.readline
n, m = map(int, input().split())
Map = []
for i in range(n):
    Map.append(input().split())
    
position = set()
check = 0
for i in range(n):
    for j in range(m):
        if Map[i][j] == '2':
            position.add((i, j))
            check = 1
            break
    if check:
        break
    
map_check = [[-1 for _ in range(m)] for _ in range(n)]
next_position = set()

count = 0
while True:
    for i in position:
        x, y = i
        if map_check[x][y] != -1:
            if Map[x][y] == '0':
                map_check[x][y] = 0
        else:
            map_check[x][y] = count
            if Map[x][y] != '0':
                next_position.update(range_check(x, y))
    if not next_position:
        break
    
    count += 1
    position.clear()
    position.update(next_position)
    next_position.clear()
    
for i in map_check:
    for j in i:
        print(j, end = ' ')
    print()