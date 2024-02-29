import sys

sys.stdin = open('input.txt')


def perm(n):
    if n == N:
        return
    else:
        for j in range(n, N):
            nums[i], nums[j] = nums[j], nums[i]
            perm(n+1)
            nums[i], nums[j] = nums[j], nums[i]


T = int(input())
for t in range(1, T+1):
    nums, limit = input().split()
    nums = list(map(int, nums))
    limit = int(limit)
    N = len(nums)
    perm(0)
    # 중복된 숫자가 있나 체크
    check_dic = {}
    check = 0
    for i in nums:
        if i in check_dic:
            check = 1
            break
        check_dic[i] = 0
    print(f"#{t} ")
    break