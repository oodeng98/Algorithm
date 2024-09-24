n = int(input())

def rec(nums, length):
    for i in range(1, length // 2 + 1):
        if nums[length-i:] == nums[length-i*2:length-i]:
            return

    if length == n:
        print(nums)
        exit(0)
        
    for i in range(1, 4):
        new_nums = nums + str(i)
        rec(new_nums, length + 1)

rec('', 0)