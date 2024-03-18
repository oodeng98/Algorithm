import sys


def merge_sort(list1):
    length = len(list1)
    if length == 1:
        return list1
    middle = length // 2
    left = list1[:middle]
    right = list1[middle:]
    left = merge_sort(left)
    right = merge_sort(right)
    if right[-1] < left[-1]:
        global count
        count += 1
    return merge(left, right)


def merge(left, right):
    result = []
    left_len = len(left)
    right_len = len(right)
    left_index = 0
    right_index = 0
    while left_index < left_len or right_index < right_len:
        if left_index < left_len and right_index < right_len:
            if left[left_index] <= right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1
        elif left_index < left_len:
            result.append(left[left_index])
            left_index += 1
        elif right_index < right_len:
            result.append(right[right_index])
            right_index += 1
    return result


sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    count = 0
    lst = merge_sort(lst)
    print(f"#{t} {lst[N//2]} {count}")