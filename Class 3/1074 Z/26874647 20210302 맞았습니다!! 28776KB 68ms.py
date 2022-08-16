import sys


def find_sequence(n, height, width):
    if n == 0:
        return 0
    result = 0
    standard = 2 ** (n - 1)  # 정사각형 한 변 길이의 반
    small_square = standard * standard
    if height < standard:  # z의 위쪽에 있을 때
        if width < standard:
            result += 0 + find_sequence(n-1, height, width)
        else:  # standard <= width
            width -= standard
            result += small_square + find_sequence(n-1, height, width)
    else:
        height -= standard
        if width < standard:
            result += small_square * 2 + find_sequence(n-1, height, width)
        else:
            width -= standard
            result += small_square * 3 + find_sequence(n-1, height, width)
    return result


input = sys.stdin.readline
num, x_target, y_target = list(map(int, input().split()))
print(find_sequence(num, x_target, y_target))