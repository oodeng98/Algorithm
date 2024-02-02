def solution(s):
    answer = s
    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for index, num in enumerate(nums):
        answer = answer.replace(num, str(index))
    return int(answer)