def solution(arr):
    if len(arr) == 1:
        return [-1]
    min_value = float('inf')
    min_index = -1
    for index, i in enumerate(arr):
        if i < min_value:
            min_value = i
            min_index = index
    arr.pop(min_index)
    return arr