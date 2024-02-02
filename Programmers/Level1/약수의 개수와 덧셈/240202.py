def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        n = 1
        check = 0
        while True:
            if n ** 2 == i:
                check = 1
                break
            if n ** 2 > i:
                break
            n += 1
        if check == 1:
            answer -= i
            continue
        answer += i
    return answer