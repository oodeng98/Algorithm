def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weekday = {3: 'SUN', 4: 'MON', 5: 'TUE', 6: 'WED', 0: 'THU', 1: 'FRI', 2: 'SAT'}
    total = 0
    for i in range(a-1):
        total += days[i]
    total += b
    return weekday[total % 7]