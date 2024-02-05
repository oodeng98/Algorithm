def solution(d, budget):
    d.sort()
    b = budget
    answer = 0
    for i in d:
        b -= i
        if b < 0:
            break
        answer += 1
    return answer