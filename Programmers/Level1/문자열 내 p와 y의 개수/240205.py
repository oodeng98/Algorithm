def solution(s):
    county = 0
    countp = 0
    for c in s:
        if c == 'y' or c == 'Y':
            county += 1
        elif c == 'p' or c == 'P':
            countp += 1
    if county == countp:
        return True
    else:
        return False