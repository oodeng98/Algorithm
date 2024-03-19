def delta(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if 0 <= a < 4 and 0 <= b < 4:
            yield a, b
 
 
def dfs(x, y, n, numbers):
    if n == 7:
        result.add(numbers)
        return
    for a, b in delta(x, y):
        dfs(a, b, n+1, numbers+arr[a][b])
 
 
T = int(input())
for t in range(1, T+1):
    arr = [input().split() for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, 1, arr[i][j])
    print(f"#{t} {len(result)}")