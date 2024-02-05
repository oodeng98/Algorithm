def solution(x):
    total = 0
    temp = x
    while temp:
        total += temp % 10
        temp //= 10
    if x % total == 0:
        return True
    return False