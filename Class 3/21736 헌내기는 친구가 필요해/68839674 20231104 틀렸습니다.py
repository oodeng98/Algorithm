import sys

def search(a, b):
    result = []
    if 0 <= a - 1:
        result.append((a - 1, b))
    if a + 1 < n:
        result.append((a + 1, b))
    if 0 <= b - 1:
        result.append((a, b - 1))
    if b + 1 < m:
        result.append((a, b + 1))
    return result

input = sys.stdin.readline
n, m = map(int, input().split())
campus = []
for i in range(n):
    campus.append(list(input().strip()))
    
campus_check = [[0 for _ in range(m)] for _ in range(n)]
position = set()
for i in range(n):
    for j in range(m):
        if campus[i][j] == 'O':
            position.add((i, j))
        elif campus[i][j] == 'X':
            campus_check[i][j] = -1
            
count = 0
next_position = set()
while True:
    for i in position:
        x, y = i
        if campus_check[x][y] == -1:
            continue
        else:
            campus_check[x][y] = -1
            if campus[x][y] == 'P':
                count += 1
            next_position.update(search(x, y))
    if not next_position:
        break
    
    position.clear()
    position.update(next_position)
    next_position.clear()
    
if count:
    print(count)
else:
    print("TT")
            
            
