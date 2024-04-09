import sys


def dfs(n, num):
    print(n, num)
    if n <= 0:
        global result
        result = max(result, int(num))
        return
    if nums[str(n)]:
        for i in nums[str(n)]:
            if i == max_value:
                pass
            dfs(n - 1, num + i)  # 빼고 다시 돌아야할거같은딩..?
    else:
        dfs(n - 1, num)


input = sys.stdin.readline
K, N = map(int, input().split())
nums = {str(i): [] for i in range(1, 10)}
for _ in range(K):
    temp = input().strip()
    nums[temp[0]].append(temp)

# 1. 나중에 더해줄 숫자 구하기
max_value = max(nums, key=lambda x: int(x))

# 2. 지금 있는 숫자들 순서 정하기
result = 0
dfs(9, '')
print(result)
'''
7
6
754
이렇게 나오면
현재 코드에서는 75476으로 표기하지만
실제로는 76754로 가는게 맞다
흐음... 이걸 어떻게 처리하지
'''