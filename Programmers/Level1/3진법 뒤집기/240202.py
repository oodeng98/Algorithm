def solution(n):
    n3 = n
    three = ''
    while n3:
        three = str(n3 % 3) + three
        n3 //= 3
    answer = 0
    for index, c in enumerate(three):
        answer += int(c) * 3 ** index
    return answer