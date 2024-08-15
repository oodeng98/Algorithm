N, S = map(int, input().split())
lst = list(map(int, input().split()))

start = 0
end = 0
total = lst[0]
result = float('inf')
while True:
    if total < S:
        end += 1
        if N <= end:
            break
        total += lst[end]
    elif S <= total:
        result = min(result, end - start + 1)
        total -= lst[start]
        start += 1
if result == float('inf'):
    result = 0
print(result)
        