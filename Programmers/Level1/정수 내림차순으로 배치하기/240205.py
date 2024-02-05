def solution(n):
    count = [0 for _ in range(10)]
    num = n
    while num:
        count[num % 10] += 1
        num //= 10
    answer = ''
    for i in range(9, -1, -1):
        while count[i]:
            answer += str(i)
            count[i] -= 1
    return int(answer)