n = int(input())
lst = list(map(int, input().split()))
left = 0
right = n - 1
mini = float('inf')
result = [lst[left], lst[right]]
while left < right:
    candidate = lst[left] + lst[right]
    if abs(mini) > abs(candidate):
        mini = candidate
        result = [lst[left], lst[right]]
    if mini == 0:
        break
    if candidate < 0:
        left += 1
    else:
        right -= 1
print(result[0], result[1])
