import sys

input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

# 내가 뽑아야 하는 수가 맨 위의 수보다 크면 push
# 내가 뽑아야 하는 수가 맨 위의 수보다 작으면 pop해야겠지
stack = [0]
i = 0
result = []
while True:
    if arr[0] > stack[-1]:
        stack.append(i+1)
        i += 1
        result.append('+')
    elif arr[0] < stack[-1]:
        result = 0
        break
    else:
        stack.pop()
        result.append('-')
        del arr[0]
    if not arr:
        break

if not result:
    print('NO')
else:
    for i in result:
        print(i)