def solution(num):
    temp = num
    answer = 0
    while temp != 1:
        if temp % 2 == 0:
            temp //= 2
        else:
            temp *= 3
            temp += 1
        answer += 1
        if answer == 500:
            return -1
    return answer