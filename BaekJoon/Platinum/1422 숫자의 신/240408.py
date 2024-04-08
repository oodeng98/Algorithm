import sys


input = sys.stdin.readline
K, N = map(int, input().split())
nums = [input().strip() for _ in range(K)]

# 1. 나중에 더해줄 숫자 구하기
max_value = max(nums, key=lambda x: int(x))

# 2. 지금 있는 숫자들 순서 정하기
# 다 같은 길이로 만들어주고 값을 비교
# 만약 값이 같은 애들이 있다면 그중에서 기존의 값이 가장 작은 애들을 찾음
max_len = len(max_value)
nums = [(int(i + (max_len - len(i)) * '0'), int(i)) for i in nums]
nums.sort(key=lambda x: x[1])
nums.sort(key=lambda x: x[0], reverse=True)
nums = [str(i[1]) for i in nums]

# 3. 결과 만들기
result = ''
check = 0
for i in range(K):
    if not check and nums[i] == max_value:
        for _ in range(N - K):
            result += max_value
        check = 1
    result += nums[i]
print(result)