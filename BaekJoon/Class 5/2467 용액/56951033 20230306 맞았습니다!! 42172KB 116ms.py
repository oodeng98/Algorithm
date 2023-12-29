n = int(input())
lst = list(map(int, input().split()))
if lst[0] >= 0:
    print(lst[0], lst[1])
    quit()
elif lst[-1] <= 0:
    print(lst[n - 2], lst[n - 1])
    quit()
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
