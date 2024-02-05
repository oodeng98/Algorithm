def solution(n):
    num = n
    answer = []
    while num:
        answer.append(num % 10)
        num //= 10
    return answer